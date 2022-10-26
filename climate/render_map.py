############################################################################################
#Könyvtárak telepítése, illetve importálása
import pip
pip.main(['install', 'osm2geojson'])
pip.main(['install', 'netCDF4'])
pip.main(['install', 'matplotlib'])

import bpy
from netCDF4 import Dataset
import matplotlib
from datetime import datetime, timedelta, date
import math
import PIL
import csv
##############################################
#Minden létező objektum törlése a jelenetből
bpy.ops.object.select_all(action="SELECT")
bpy.ops.object.delete(use_global=False)

############################################################################################
#JELENET PARAMÉTEREINEK BEÁLLÍTÁSA
#Emission color
bpy.data.worlds["World"].node_tree.nodes["Principled BSDF"].inputs[19].default_value = (1, 1, 1, 1)

#Emission strength
bpy.data.worlds["World"].node_tree.nodes["Principled BSDF"].inputs[20].default_value = 0.07

#Scene color
bpy.context.scene.world.color = (0.85, 0.85, 0.85)

############################################################################################
#OBJEKTUMOK LÉTREHOZÁSA
#SZÖVEG OBJEKTUM
#Dátum kiszámítása
day_selected = 3835
start_date = date(2011, 1, 1)
end_date = start_date + timedelta(days=day_selected)
year, month, day = end_date.strftime("%Y"), end_date.strftime("%m"), end_date.strftime("%d")
end_date_str = year + ". " + month + ". " + day + "."

#Szöveg objektum létrehozása, pozicionálása, méretezése
font_curve = bpy.data.curves.new(type="FONT", name="Font Curve")
font_curve.body = end_date_str
font_obj = bpy.data.objects.new(name="Font Object", object_data=font_curve)
font_obj.location = (16.763, 44.916, 0)
font_obj.scale = (1, 1, 0)

#Fekete material hozzárendelése a szöveghez
text_material = bpy.data.materials.new("Text")
text_material.diffuse_color = (0,0,0,1)
font_obj.data.materials.append(text_material)
bpy.context.scene.collection.objects.link(font_obj)

#FÉNYFORRÁS LÉTREHOZÁSA
light_data = bpy.data.lights.new(name='Light', type='SUN')
light = bpy.data.objects.new(name='Light', object_data=light_data)

light.location = (19.29, 45, 9.1334)
light_data.energy = 1
light_data.color = (1,1,1)
bpy.context.collection.objects.link(light)

bpy.context.scene.eevee.use_gtao = True #ambient occlusion

#KAMERA LÉTREHOZÁSA
camera = bpy.data.cameras.new('Camera')
camera.lens=35
camera.type='PERSP'

camera_obj = bpy.data.objects.new('CameraObj', camera)
#A location koordinátáit az empty objektum koordinátáihoz viszonyítva kell megadni
camera_obj.location = (-2.6688, -6.5755, 3.8764)
camera_obj.rotation_euler = (1.0210, 0, -0.3804)
bpy.context.collection.objects.link(camera_obj)
bpy.context.scene.camera = camera_obj

#ÜRES OBJEKTUM LÉTREHOZÁSA
#A térkép közepén kerül elhelyezésre, ekörül fog körbeforogni a kamera
empty = bpy.data.objects.new("empty", None)
empty.location=(19.25, 47.05, 0.030667)
empty.scale=(1,1,1)
bpy.context.collection.objects.link(empty)

#Parent-ként a kamerához kell rendelni
camera_obj.parent = empty
############################################################################################
#NETCDF ADATHALMAZ BEOLVASÁSA
source = "datasets/tg_ens_mean_0.1deg_reg_2011-2021_v25.0e.nc_sliced"
ds = Dataset(source)

lats = ds.variables['latitude'][:]
lons = ds.variables['longitude'][:]
dates = ds.variables['time'][:]
temp = ds.variables['tg'][:]

#színskála létrehozása
cmap = matplotlib.cm.get_cmap('nipy_spectral')

#koordináták, azok magasságának beolvasása a csv fájlból.
coords = []
f = open('elevation.csv', newline='')
reader = csv.reader(f, delimiter=',')

#header sor kihagyása
next(reader, None)
     
for row in reader:
    coords.append([float(row[1]), float(row[0]), float(row[2]), cmap((temp[day_selected, int(row[3]), int(row[4])] + 20) / 60)])

#Az oszlopok létrehozása
for coord in coords:
    #Material létrehozása, a színének meghatározása a colormap alapján
    material = bpy.data.materials.new('Material')
    
    material.use_nodes = True
    if material.node_tree:
        material.node_tree.links.clear()
        material.node_tree.nodes.clear()
    
    nodes = material.node_tree.nodes
    links = material.node_tree.links
    
    output = nodes.new(type='ShaderNodeOutputMaterial')
    shader = nodes.new(type='ShaderNodeBsdfVelvet')
    nodes['Velvet BSDF'].inputs[0].default_value = (coord[3][0], coord[3][1], coord[3][2], 1)
    links.new(shader.outputs[0], output.inputs[0])
    
    #Az oszlop létrehozása, lekerekített élek (bevel) hozzárendelése
    bpy.ops.mesh.primitive_cube_add(size=2, enter_editmode=False, align='WORLD',
    location=(coord[0], coord[1], coord[2]/2500), scale=(0.04, 0.04, coord[2]/2500))
    bpy.context.object.data.materials.append(material)
    bevel = bpy.context.object.modifiers.new('Bevel', 'BEVEL')
    bevel.width = 0.005
    bevel.segments = 16

#RENDER BEÁLLÍTÁSOK
#képkockaszám megadása - ennyi áll elő egy körbeforgás alatt
frames = 64

#Felbontás, minőség beállítása
bpy.context.scene.render.resolution_x = 1280
bpy.context.scene.render.resolution_y = 720
bpy.context.scene.render.resolution_percentage = 100
bpy.context.scene.frame_end = 1

#A kamera forgatása, és a képkockák renderelése
for frame in range(frames):
    bpy.context.scene.render.filepath = "output{0}".format(frame+1)
    empty.rotation_euler[2] += (2*math.pi) / frames
    camera_obj.keyframe_insert(data_path="location", index=-1, frame=frame)
    bpy.ops.render.render(animation=True)
    

#Az előállt képkockák GIF formátumba mentése
gif_frames = []

#Egy képkocka hossza, milliszekundumban
duration = 50

for frame in range(frames):
  frame = PIL.Image.open("output{0}0001.png".format(frame+1))
  gif_frames.append(frame)

output = 'output.gif'
gif_frames[0].save(output, format='GIF',append_images = gif_frames[1: ], save_all = True, duration=duration, loop=0)


    


