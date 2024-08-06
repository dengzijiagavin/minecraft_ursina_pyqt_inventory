import sys
from easygui import *
import sys
from PyQt5 import QtWidgets,uic

zhujiemian=uic.loadUiType('zhujiemian.ui')[0]
class Zjm(QtWidgets.QMainWindow,zhujiemian):
    def __init__(self,parent=None):
        QtWidgets.QMainWindow.__init__(self,parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.danrenyouxi)
        self.pushButton_2.clicked.connect(self.duorenyouxi)
        self.pushButton_3.clicked.connect(self.pifuzhanghao)
        self.pushButton_4.clicked.connect(self.zuozhe)
    def danrenyouxi(self):
        msgbox('关掉主窗口即可运行游戏')

    def duorenyouxi(self):
        msgbox('多人游戏暂未开通','wanning')
    def pifuzhanghao(self):
        q=buttonbox('哪个是你的？',choices=list(map(str,open('zhanghao.txt','r').read().split(' ')))+['New'])
        if q=='New':
            e=(open('zhanghao.txt', 'a'))
            e.write(' '+enterbox())
            e.close()
    def zuozhe(self):
        msgbox('作者是邓梓嘉12岁，作于2024.8.4日')
app = QtWidgets.QApplication(sys.argv)
mywindow=Zjm()
mywindow.show()
app.exec_()
def gamesetting():
    global generatingTerrain
    if held_keys['escape']:
        mouse.locked = False
        q = buttonbox('设置界面', choices=['play', 'Quit', 'settings'])
        if q == 'play':
            mouse.locked = True
        elif q == 'Quit':
            quit()
            mouse.locked = True
        else:
            q = buttonbox('这个是十分危险的！你确定吗，小心bugs',
                          choices=['我就犯贱', '我走了'])
            if q != '我走了':
                try:
                    subject = FirstPersonController()
                    q = choicebox('修改项选择',
                                  choices=['close', 'window.color(rgb', 'subject.gravity', 'subject.height = 1.0',
                                           'subject.runSpeed = 8', 'subject.walkSpeed = 12', 'camera.dash = 10',
                                           'camera.fov = origFOV = 63', 'subject.cursor.color = color.white',
                                           'subject.blockType = None', 'subject.frog = False',
                                           'subject.cursor.visible = True',
                                           'window.fullscreen=False'])
                    if q == 'window.color(rgb':
                        w = list(map(int, enterbox('rgb用空格隔开').split(' ')))
                        window.color = color.rgb(w[0], w[1], w[2])
                    elif q == 'subject.gravity':
                        w = list(map(int, enterbox('subject.gravity').split(' ')))
                        subject.gravity = w[0]
                    elif q == 'subject.gravity':
                        w = list(map(int, enterbox('subject.gravity').split(' ')))
                        subject.gravity = w[0]
                    elif q == 'subject.height = 1.0':
                        w = list(map(int, enterbox('subject.height = 1.0').split(' ')))
                        subject.gravity = w[0]
                        subject.camera_pivot.y = subject.height
                    elif q == 'subject.runSpeed = 8':
                        w = list(map(int, enterbox('subject.runSpeed = 8').split(' ')))
                        subject.runSpeed = w[0]
                    elif q == 'subject.walkSpeed = 12':
                        w = list(map(int, enterbox('subject.walkSpeed = 12').split(' ')))
                        subject.walkSpeed = w[0]
                    elif q == 'camera.dash = 10':
                        w = list(map(int, enterbox('camera.dash = 10').split(' ')))
                        camera.dash = w[0]
                    elif q == 'subject.frog = False':
                        w = list(map(int, enterbox('subject.frog = False').split(' ')))
                        subject.frog = w[0]
                    elif q == 'subject.cursor.visible = True':
                        w = list(map(int, enterbox('subject.cursor.visible = True').split(' ')))
                        subject.cursor.visible = w[0]
                    elif q == 'subject.cursor.color = color.white':
                        w = list(map(int, enterbox('subject.cursor.color = color.white').split(' ')))
                        subject.cursor.color = w[0]
                    elif q == 'subject.blockType = None':
                        w = list(map(int, enterbox('subject.blockType = None').split(' ')))
                        subject.blockType = w[0]
                    elif q == 'camera.fov = origFOV = 63':
                        w = list(map(int, enterbox('camera.fov = origFOV = 63').split(' ')))
                        camera.fov = origFOV = w[0]
                    elif q == 'window.fullscreen=False':
                        w = list(map(int, enterbox('window.fullscreen=False').split(' ')))
                        window.fullscreen = w[0]
                    else:
                        pass
                except:
                    window.color = color.rgb(0, 200, 225)
                    # indra = Sky()
                    # indra.color = window.color
                    subject = FirstPersonController()
                    subject.gravity = 0.0
                    subject.cursor.visible = True
                    subject.cursor.color = color.white
                    subject.height = 1.62  # Minecraft eye-level?
                    subject.camera_pivot.y = subject.height
                    subject.frog = False  # For jumping...
                    subject.runSpeed = 8
                    subject.walkSpeed = 12
                    subject.blockType = None  # Current building mineral.
                    camera.dash = 10  # Rate at which fov changes when running.
                    camera.fov = origFOV = 63
                    window.fullscreen = False
            else:
                mouse.locked = True
from ursina import *
# Instantiate ursina here, so that textures can be
# loaded without issue in other modules :)
app = Ursina()
from ursina import Vec3, Vec4
from ursina.prefabs.first_person_controller import FirstPersonController
from mesh_terrain import MeshTerrain
from flake import SnowFall
import random as ra
from bump_system import *
from save_load_system import saveMap, loadMap
from inventory_system import *
from random import *
inventory = []
window.color = color.rgb(0, 200, 225)
# indra = Sky()
# indra.color = window.color
subject = FirstPersonController()
subject.gravity = 0.0
subject.cursor.visible = True
subject.cursor.color = color.white
subject.height = 1.62  # Minecraft eye-level?
subject.camera_pivot.y = subject.height
subject.frog = False  # For jumping...
subject.runSpeed = 8
subject.walkSpeed = 12
subject.blockType = None  # Current building mineral.
camera.dash = 10  # Rate at which fov changes when running.
camera.fov = origFOV = 63
# *** - see inventory_system.py
# window.fullscreen=False
terrain = MeshTerrain(subject, camera)
# snowfall = SnowFall(subject)
# How do you at atmospheric fog?
scene.fog_density = (0, 75)
# scene.fog_color=indra.color
scene.fog_color = color.white
generatingTerrain = True
# Generate our terrain 'chunks'.
for i in range(4):
    terrain.genTerrain()
# For loading in a large terrain at start.
# loadMap(subject,terrain)
grass_audio = Audio('step.ogg', autoplay=False, loop=False)
snow_audio = Audio('snowStep.mp3', autoplay=False, loop=False)
grass_audio.volume = 0.1
pX = subject.x
pZ = subject.z
'''
==================================================================
'''
create_new_world = 0
inventory_blocks = []
inventory_opened = 0
try:
    world = np.load("world.npy")
except:
    print("World not found...")
    create_new_world = 1
    world = np.zeros([60, 60, 60])
grass_texture = load_texture('assets/grass_block.png')
stone_texture = load_texture('assets/stone_block.png')
brick_texture = load_texture('assets/brick_block.png')
dirt_texture = load_texture('assets/dirt_block.png')
wood_texture = load_texture('assets/wood_block.png')
leave_texture = load_texture('assets/leaves_block.png')
sand_texture = load_texture('assets/sand_block.png')
cactus_texture = load_texture('assets/cactus_block.png')
planks_texture = load_texture('assets/planks_block.png')
brick_grey_texture = load_texture('assets/brick_grey_block.png')
glass_texture = load_texture('assets/glass_block.png')
furnace_texture = load_texture('assets/furnace_block.png')
crafting_texture = load_texture('assets/crafting_block.png')
grass_texture2 = load_texture('assets/grass.png')
sky_texture = load_texture('assets/skybox.png')
arm_texture = load_texture('assets/arm_texture.png')
water_texture = load_texture('assets/water.png')
wheat_texture = load_texture('assets/wheat.png')
snow_texture = load_texture('assets/snow.png')
apple_texture = load_texture('assets/apple.png')
punch_sound = Audio('assets/punch_sound', loop=False, autoplay=False)
block_pick = 1
block_texture = grass_texture
window.fps_counter.enabled = False
window.exit_button.visible = False
class Inventory(Button):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(.5, .8),
            origin=(-.5, .5),
            position=(-.3, .4),
            texture='white_cube',
            texture_scale=(5, 8),
            color=color.dark_gray
        )
        self.item_parent = Entity(parent=self, scale=(1 / 5, 1 / 8))
    def find_free_spot(self):
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
        for y in range(8):
            for x in range(5):
                if not (x, -y) in taken_spots:
                    return (x, -y)
    def append(self, item):
        name = item.replace('blocks/', ' ').title()
        blocks = Button(
            parent=inventory.item_parent,
            texture=item,
            color=color.white,
            tooltip=Tooltip('close inventory'),
            origin=(-.5, .5),
            position=self.find_free_spot(),
            z=-.1,
        )
        inventory_blocks.append(blocks)
        inventory_blocks[0].on_click = brick
        try:
            inventory_blocks[1].on_click = grey_brick
            try:
                inventory_blocks[2].on_click = cactus
                try:
                    inventory_blocks[3].on_click = crafting_table
                    try:
                        inventory_blocks[4].on_click = dirt
                        try:
                            inventory_blocks[5].on_click = furnace
                            try:
                                inventory_blocks[6].on_click = grass
                                try:
                                    inventory_blocks[7].on_click = leaves
                                    try:
                                        inventory_blocks[8].on_click = planks
                                        try:
                                            inventory_blocks[9].on_click = sand
                                            try:
                                                inventory_blocks[10].on_click = stone
                                                try:
                                                    inventory_blocks[11].on_click = wood
                                                    try:
                                                        inventory_blocks[12].on_click = glass
                                                        try:
                                                            inventory_blocks[13].on_click = water
                                                            try:
                                                                inventory_blocks[14].on_click = grass_other
                                                                try:
                                                                    inventory_blocks[15].on_click = wheat
                                                                    try:
                                                                        inventory_blocks[16].on_click = snow
                                                                        try:
                                                                            inventory_blocks[17].on_click = apple
                                                                            try:
                                                                                inventory_blocks[
                                                                                    39].on_click = close
                                                                            except:
                                                                                pass
                                                                        except:
                                                                            pass
                                                                    except:
                                                                        pass
                                                                except:
                                                                    pass
                                                            except:
                                                                pass
                                                        except:
                                                            pass
                                                    except:
                                                        pass
                                                except:
                                                    pass
                                            except:
                                                pass
                                        except:
                                            pass
                                    except:
                                        pass
                                except:
                                    pass
                            except:
                                pass
                        except:
                            pass
                    except:
                        pass
                except:
                    pass
            except:
                pass
        except:
            pass
        # name = item.replace('_', ' ').title()
        blocks.tooltip = Tooltip(name)
        blocks.tooltip.background.color = color.color(0, 0, 0, .8)
def brick():
    global block_pick, block_texture
    block_texture = brick_texture
    block_pick = 3
def grey_brick():
    global block_pick, block_texture
    block_texture = brick_grey_texture
    block_pick = 10
def cactus():
    global block_pick, block_texture
    block_texture = cactus_texture
    block_pick = 8
def crafting_table():
    global block_pick, block_texture
    block_texture = crafting_texture
    block_pick = 12
def dirt():
    global block_pick, block_texture
    block_texture = dirt_texture
    block_pick = 4
def furnace():
    global block_pick, block_texture
    block_texture = furnace_texture
    block_pick = 13
def grass():
    global block_pick, block_texture
    block_texture = grass_texture
    block_pick = 1
def leaves():
    global block_pick, block_texture
    block_texture = leave_texture
    block_pick = 6
def planks():
    global block_pick, block_texture
    block_texture = planks_texture
    block_pick = 9
def sand():
    global block_pick, block_texture
    block_texture = sand_texture
    block_pick = 7
def stone():
    global block_pick, block_texture
    block_texture = stone_texture
    block_pick = 2
def wood():
    global block_pick, block_texture
    block_texture = wood_texture
    block_pick = 5
def glass():
    global block_pick, block_texture
    block_texture = glass_texture
    block_pick = 11
def grass_other():
    global block_pick, block_texture
    block_texture = grass_texture2
    block_pick = 14
def water():
    global block_pick, block_texture
    block_texture = water_texture
    block_pick = 15
def wheat():
    global block_pick, block_texture
    block_texture = wheat_texture
    block_pick = 16
def snow():
    global block_pick, block_texture
    block_texture = snow_texture
    block_pick = 17
def apple():
    global block_pick, block_texture
    block_texture = apple_texture
    block_pick = 18
class Voxel(Button):
    def __init__(self, position=(0, 0, 0), texture=grass_texture):
        super().__init__(
            parent=scene,
            position=position,
            model='assets/block1',
            origin_y=0.5,
            texture=texture,
            color=color.color(0, 0, uniform(0.9, 1)),
            scale=0.5)
    def input(self, key):
        global inventory_opened


        if self.hovered:
            if key == 'right mouse down':
                pos = self.position + mouse.normal
                punch_sound.play()
                if block_pick == 1:
                    voxel = Voxel(position=pos, texture=grass_texture)
                    # print(pos)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                # print(world[int(pos[0]), int(pos[1]), int(pos[2])])
                if block_pick == 2:
                    voxel = Voxel(position=pos, texture=stone_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 3:
                    voxel = Voxel(position=pos, texture=brick_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 4:
                    voxel = Voxel(position=pos, texture=dirt_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 5:
                    voxel = Voxel(position=pos, texture=wood_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 6:
                    voxel = Voxel(position=pos, texture=leave_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 7:
                    voxel = Voxel(position=pos, texture=sand_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 8:
                    voxel = Voxel(position=pos, texture=cactus_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 9:
                    voxel = Voxel(position=pos, texture=planks_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 10:
                    voxel = Voxel(position=pos, texture=brick_grey_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 11:
                    voxel = Voxel(position=pos, texture=glass_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 12:
                    voxel = Voxel(position=pos, texture=crafting_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 13:
                    voxel = Voxel(position=pos, texture=furnace_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 14:
                    voxel = Voxel(position=pos, texture=grass_texture2)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 15:
                    voxel = Voxel(position=pos, texture=water_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 16:
                    voxel = Voxel(position=pos, texture=wheat_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 17:
                    voxel = Voxel(position=pos, texture=snow_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
                if block_pick == 18:
                    voxel = Voxel(position=pos, texture=apple_texture)
                    world[int(pos[0]), int(pos[1]), int(pos[2])] = block_pick
            if key == 'left mouse down':
                pos = self.position
                world[int(pos[0]), int(pos[1]), int(pos[2])] = 0
                # print(world[int(pos[0]), int(pos[1]), int(pos[2])])
                punch_sound.play()
                destroy(self)
class Sky(Entity):
    def __init__(self):
        super().__init__(
            parent=scene,
            model='sphere',
            texture=sky_texture,
            scale=150,
            double_sided=True)
class Hand(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/arm',
            texture=arm_texture,
            scale=0.2,
            rotation=Vec3(150, -20, 0),
            position=Vec2(0.9, -0.6))
    def active(self):
        self.position = Vec2(0.8, -0.5)
    def passive(self):
        self.position = Vec2(0.9, -0.6)
class Block(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='assets/block',
            texture=block_texture,
            scale=0.2,
            rotation=[Vec3(0, 1, 0),
                      Vec3(0, -1, 0),
                      Vec3(-1, 0, 0),
                      Vec3(1, 0, 0),
                      Vec3(0, 0, -1),
                      Vec3(0, 0, 1)],
            position=Vec2(-0.6, -0.4))
    def active(self):
        self.position = Vec2(-0.5, -0.3)
    def passive(self):
        self.position = Vec2(-0.6, -0.4)
if create_new_world == 1:
    for z in range(40):
        for x in range(40):
            voxel = Voxel(position=(x, 0, z))
            world[x, 0, z] = 1
else:
    for x in range(40):
        for y in range(40):
            for z in range(40):
                if world[x, y, z] == 1:
                    texture = grass_texture
                if world[x, y, z] == 2:
                    texture = stone_texture
                if world[x, y, z] == 3:
                    texture = brick_texture
                if world[x, y, z] == 4:
                    texture = dirt_texture
                if world[x, y, z] == 5:
                    texture = wood_texture
                if world[x, y, z] == 6:
                    texture = leave_texture
                if world[x, y, z] == 7:
                    texture = sand_texture
                if world[x, y, z] == 8:
                    texture = cactus_texture
                if world[x, y, z] == 9:
                    texture = planks_texture
                if world[x, y, z] == 10:
                    texture = brick_grey_texture
                if world[x, y, z] == 11:
                    texture = glass_texture
                if world[x, y, z] == 12:
                    texture = crafting_texture
                if world[x, y, z] == 13:
                    texture = furnace_texture
                if world[x, y, z] == 14:
                    texture = grass_texture2
                if world[x, y, z] == 15:
                    texture = water_texture
                if world[x, y, z] == 16:
                    texture = wheat_texture
                if world[x, y, z] == 17:
                    texture = snow_texture
                if world[x, y, z] == 18:
                    texture = apple_texture
                if world[x, y, z] != 0:
                    voxel = Voxel(position=(x, y, z), texture=texture)
inventory_opened = 0
'''
==================================================================
'''
def input(key):
    global generatingTerrain
    terrain.input(key)
    if key == 'g':
        generatingTerrain = not generatingTerrain
    # Jumping...
    if key == 'space': subject.frog = True
    # Saving and loading...
    if key == 'm': saveMap(subject.position, terrain.td)
    if key == 'l': loadMap(subject, terrain)

    # Inventory access.
    inv_input(key, subject, mouse)
count = 0
earthcounter = 0
earthquake_ON = False
def update():
    global count, pX, pZ, earthcounter, origFOV, subject
    global block_pick, inventory_opened, inventory, block_texture
    block.texture = block_texture
    if held_keys['right mouse']:
        hand.active()
    else:
        hand.passive()
    if held_keys['left mouse']:
        block.active()
    else:
        block.passive()
    if held_keys['r']:
        np.save("world.npy", world)
        print("World saved...")
    if held_keys['i']:
        inventory_opened = 1
        inventory_blocks.clear()
        try:
            destroy(inventory)
            # destroy(add_item_button)
            inventory = Inventory()
            add_item()
            mouse.locked = False
            mouse.visible = True
            mouse.enabled = True
        # add_button()
        except:
            inventory = Inventory()
            add_item()
            mouse.locked = False
            mouse.visible = True
            mouse.enabled = True
        # add_button()
    '''
    if held_keys['Tab']:
        subject = FirstPersonController(jump_height=100, )'''
    if held_keys['c']:
        inventory_opened = 0
        close()
        mouse.locked = True
        mouse.visible = False
        mouse.enabled = True
    # Highlight terrain block for mining/building...
    terrain.update()
    # Handle mob ai.
    mob_movement(grey, subject.position, terrain.td)
    count += 1
    if count >= 1:
        count = 1
        # Generate terrain at current swirl position.
        if generatingTerrain:
            terrain.genTerrain()
            # for i in range(1):
            # terrain.genTerrain()
    # Change subset position based on subject position.
    if abs(subject.x - pX) > 1 or abs(subject.z - pZ) > 1:
        pX = subject.x
        pZ = subject.z
        terrain.swirlEngine.reset(pX, pZ)
        # Sound :)
        if subject.y > 4:
            if snow_audio.playing == False:
                snow_audio.pitch = ra.random() + 0.25
                snow_audio.play()
        elif grass_audio.playing == False:
            grass_audio.pitch = ra.random() + 0.7
            grass_audio.play()
    # *******
    #  Earthquake experiment!
    if earthquake_ON:
        earth_amp = 0.1
        earth_freq = 0.5
        earthcounter += earth_freq
        for h in terrain.subsets:
            h.y = (math.sin(terrain.subsets.index(h) +
                            earthcounter) * earth_amp)  # *time.dt
    # *******
    # Walk on solid terrain, and check wall collisions.
    '=================================================================================================='
    bumpWall(subject, terrain)
    '=================================================================================================='
    # Running and dash effect.
    if held_keys['shift'] and held_keys['w']:
        subject.speed = subject.runSpeed
        if camera.fov < 100:
            camera.fov += camera.dash * time.dt
    else:
        subject.speed = subject.walkSpeed
        if camera.fov > origFOV:
            camera.fov -= camera.dash * 4 * time.dt
            if camera.fov < origFOV: camera.fov = origFOV
    if held_keys['escape']:
        mouse.locked = False
        q = buttonbox('设置界面', choices=['play', 'Quit', 'settings'])
        if q == 'play':
            mouse.locked = True
        elif q == 'Quit':
            quit()
            mouse.locked = True
        else:
            q = buttonbox('这个是十分危险的！你确定吗，小心bugs',
                          choices=['我就犯贱', '我走了'])
            if q != '我走了':
                try:
                    subject = FirstPersonController()
                    q = choicebox('修改项选择',
                                  choices=['close', 'window.color(rgb', 'subject.gravity', 'subject.height = 1.0',
                                           'subject.runSpeed = 8', 'subject.walkSpeed = 12', 'camera.dash = 10',
                                           'camera.fov = origFOV = 63', 'subject.cursor.color = color.white',
                                           'subject.blockType = None', 'subject.frog = False',
                                           'subject.cursor.visible = True',
                                           'window.fullscreen=False'])
                    if q == 'window.color(rgb':
                        w = list(map(int, enterbox('rgb用空格隔开').split(' ')))
                        window.color = color.rgb(w[0], w[1], w[2])
                    elif q == 'subject.gravity':
                        w = list(map(int, enterbox('subject.gravity').split(' ')))
                        subject.gravity = w[0]
                    elif q == 'subject.gravity':
                        w = list(map(int, enterbox('subject.gravity').split(' ')))
                        subject.gravity = w[0]
                    elif q == 'subject.height = 1.0':
                        w = list(map(int, enterbox('subject.height = 1.0').split(' ')))
                        subject.gravity = w[0]
                        subject.camera_pivot.y = subject.height
                    elif q == 'subject.runSpeed = 8':
                        w = list(map(int, enterbox('subject.runSpeed = 8').split(' ')))
                        subject.runSpeed = w[0]
                    elif q == 'subject.walkSpeed = 12':
                        w = list(map(int, enterbox('subject.walkSpeed = 12').split(' ')))
                        subject.walkSpeed = w[0]
                    elif q == 'camera.dash = 10':
                        w = list(map(int, enterbox('camera.dash = 10').split(' ')))
                        camera.dash = w[0]
                    elif q == 'subject.frog = False':
                        w = list(map(int, enterbox('subject.frog = False').split(' ')))
                        subject.frog = w[0]
                    elif q == 'subject.cursor.visible = True':
                        w = list(map(int, enterbox('subject.cursor.visible = True').split(' ')))
                        subject.cursor.visible = w[0]
                    elif q == 'subject.cursor.color = color.white':
                        w = list(map(int, enterbox('subject.cursor.color = color.white').split(' ')))
                        subject.cursor.color = w[0]
                    elif q == 'subject.blockType = None':
                        w = list(map(int, enterbox('subject.blockType = None').split(' ')))
                        subject.blockType = w[0]
                    elif q == 'camera.fov = origFOV = 63':
                        w = list(map(int, enterbox('camera.fov = origFOV = 63').split(' ')))
                        camera.fov = origFOV = w[0]
                    elif q == 'window.fullscreen=False':
                        w = list(map(int, enterbox('window.fullscreen=False').split(' ')))
                        window.fullscreen = w[0]
                    else:
                        pass
                except:
                    window.color = color.rgb(0, 200, 225)
                    # indra = Sky()
                    # indra.color = window.color
                    subject = FirstPersonController()
                    subject.gravity = 0.0
                    subject.cursor.visible = True
                    subject.cursor.color = color.white
                    subject.height = 1.62  # Minecraft eye-level?
                    subject.camera_pivot.y = subject.height
                    subject.frog = False  # For jumping...
                    subject.runSpeed = 8
                    subject.walkSpeed = 12
                    subject.blockType = None  # Current building mineral.
                    camera.dash = 10  # Rate at which fov changes when running.
                    camera.fov = origFOV = 63
                    window.fullscreen = False
            else:
                mouse.locked = True
from mob_system import *
if __name__ == '__main__':
    sky = Sky()
    hand = Hand()
    block = Block()
    block.texture = block_texture
    if inventory_opened == 1:
        block.texture = block_texture
        inventory = Inventory()
    if inventory_opened == 0:
        block.texture = block_texture
        # subject = FirstPersonController(origin_y=-.5, origin_x=5)
        subject.jump_height = 1
        subject.mouse_sensitivity = Vec2(40, 40)

    def add_item():
        global inventory_opened, inventory
        if inventory_opened == 1:
            # inventory = ['grass block', 'stone block', 'brick_block', 'dirt_block', 'grey brick block', 'cactus block', 'crafting_table', 'furnace block', 'glass block', 'leaves block', 'planks block', 'sand block', 'wood block']
            inventory.append('blocks/brick block')
            inventory.append('blocks/grey brick block')
            inventory.append('blocks/cactus block')
            inventory.append('blocks/crafting table')
            inventory.append('blocks/dirt block')
            inventory.append('blocks/furnace')
            inventory.append('blocks/grass block')
            inventory.append('blocks/leaves block')
            inventory.append('blocks/planks block')
            inventory.append('blocks/sand block')
            inventory.append('blocks/stone block')
            inventory.append('blocks/wood block')
            inventory.append('blocks/glass block')
            inventory.append('blocks/water block')
            inventory.append('assets/grass')
            inventory.append('assets/wheat')
            inventory.append('blocks/voxelTile_02')
            inventory.append('assets/apple')
            for empty in range(21):
                inventory.append('blocks/ ')
            inventory.append('blocks/close (c)')
    def close():
        global add_item_button
        destroy(inventory)
        inventory_opened = 0
        mouse.locked = True
        mouse.visible = False
        mouse.enabled = True
        block.texture = block_texture
        '''
        if inventory_opened == 0:
            subject = FirstPersonController(jump_height = 1, )'''
    for i in range(1):
        add_item()
app.run()