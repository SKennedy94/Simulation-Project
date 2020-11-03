import math
from vpython import *
from planet import Planet

scene.width = 1200
scene.height = 800
scene.userspin = False

scene.lights = []
scene.autoscale = False

time = 0
deltaTime = 360

skybox = box(pos=vector(0,0,0),length=200, height=200, width=200,texture="images/stars.jpg")
.0000000147e24
# inflate distance by 3
Sun = Planet(1.989e30, 0, 1 , 0,[], "images/sun.jpg")

Mercury = Planet (0.330e24, 57.9e9, .05, 2, False, "images/mercury.jpg")

Venus = Planet (4.87e24, 108.2e9, .15,3, False, "images/venus.jpg")

Earth = Planet(5.973e24*2, 149.6e9, .25,4, False, "images/earth.jpg")
Moon = Planet(0.073e24/2, 384400000, .03, 4.35,True, "images/moon.jpg")

Mars = Planet (0.64171e24, 227.9e9, .275, 5, False, "images/mars.jpg")
Deimos = Planet(0.0000000147e24, 23460000, .03, 5.35,True, "images/moon.jpg")
Phobos = Planet( 0.00000001065e24,92070000 , .03, 5.35,True, "images/moon.jpg")

Jupiter = Planet (1898e24, 778.6e9, .6, 6.5,False, "images/jupiter.jpg")
Callisto = Planet (.000000000107e24,1882700, 0.03, 7.4, True, "images/moon.jpg")
Europa = Planet (.0000000000479e24,671100, 0.03, 7.5, True, "images/moon.jpg")
Io = Planet (.00000000148e24,1070400, 0.03, 7.6, True, "images/moon.jpg")
Ganymede = Planet (.00000000000893,421800, 0.03, 7.3, True, "images/moon.jpg")

Saturn = Planet (568e24, 1443.5e9, .45, 9,False, "images/saturn.jpg")

Uranus = Planet (86.8e24, 2872.5e9,.4, 11,False, "images/uranus.jpg")

Neptune = Planet (102e24, 4495.1e9, .4, 13,False, "images/neptune.jpg")

Pluto = Planet (0.0146e24, 5906.4e9, .05, 15,False, "images/mercury.jpg")

Sun._sphere.emissive = True
scene.ambient = color.white

scene.camera.follow(Sun._sphere)

def S(s): 
    if s.value > 0:
        global deltaTime
        deltaTime = 360 * (s.value*100)
slider( bind=S, text='Time')
scene.append_to_caption('\n\n')

def M(m):
    if m.selected == 'Sun':
        scene.camera.follow(Sun._sphere)
    elif m.selected == 'Mercury':
        scene.camera.follow(Mercury._sphere)
    elif m.selected == 'Venus':
        scene.camera.follow(Venus._sphere)
    elif m.selected == 'Earth':
        scene.camera.follow(Earth._sphere)
    elif m.selected == 'Mars':
        scene.camera.follow(Mars._sphere)
    elif m.selected == 'Jupiter':
        scene.camera.follow(Jupiter._sphere)
    elif m.selected == 'Saturn':
        scene.camera.follow(Saturn._sphere)
    elif m.selected == 'Uranus':
        scene.camera.follow(Uranus._sphere)
    elif m.selected == 'Neptune':
        scene.camera.follow(Neptune._sphere)
    elif m.selected == 'Pluto':
        scene.camera.follow(Pluto._sphere)
        
menu( choices=['Sun','Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto',], bind=M )
scene.append_to_caption('\n\n')

def keyInput(evt):
    s = evt.key
    right = scene.forward.cross(scene.up)
    if (s == 'right'):
        scene.camera.rotate(angle=0.03, axis=scene.camera.up, origin=scene.camera.pos)
    if (s == 'left'):
        scene.camera.rotate(angle=-0.03, axis=scene.camera.up, origin=scene.camera.pos)
    if (s == 'up'):
        scene.camera.rotate(angle=-0.05, axis=right, origin=scene.camera.pos)
    if (s == 'down'):
        scene.camera.rotate(angle=0.03, axis=right, origin=scene.camera.pos)

scene.bind('keydown', keyInput)

while True:
    rate(60)
    
    Mercury.update(time,deltaTime,Sun)
    
    Venus.update(time,deltaTime,Sun)
    
    Earth.update(time,deltaTime,Sun)
    
    Moon.update(time,deltaTime,Earth)
    
    Mars.update(time,deltaTime,Sun)
    Deimos.update(time,deltaTime,Mars)
    Phobos.update(time,deltaTime,Mars)
    
    Jupiter.update(time,deltaTime,Sun)
    Callisto.update(time,deltaTime,Jupiter)
    Europa.update(time,deltaTime,Jupiter)
    Io.update(time,deltaTime,Jupiter)
    Ganymede.update(time,deltaTime,Jupiter)
    
    Saturn.update(time,deltaTime,Sun)
    
    Uranus.update(time,deltaTime,Sun)
    
    Neptune.update(time,deltaTime,Sun)
    
    Pluto.update(time,deltaTime,Sun)

    time+=deltaTime
    



