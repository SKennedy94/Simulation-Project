import math
from vpython import *

# Gravitational Constant
Gravity = 6.67e-11

class Planet():
    '''
    __init__ function takes mass of the planet (scientific notation),
    distance from the sun, the radius of the planet (scaled to look better),
    color of the planet, and a list of moons (type Planet)
    '''

    # distance from sun
    # angular velocity = sqrt(force/(mass * distance))
    # theta = angular velocity * timestep
    # velocity = angular velocity * distance
    def __init__(self, mass, distance, radius, x, moon, Texture):
        self._mass = mass               # mass of the planet
        self._distance = distance       # distance from attrator
        self._radius = radius           # radius of the planet (scaled down)
        self._moon = moon               # if is moon
        self._theta = 0                 # angular position       
        self._angularVelocity = 0       # angular velocity
        self._force = 0                 #
        self._position = 0              #
        self._worldPos = x
        
        if(self._moon):
            self._sphere = sphere(pos=vector(self._worldPos,0,0),color=color.white, texture=Texture, radius=self._radius, make_trail=True, trail_type="points", interval=10, retain=20)
        else:    
            self._sphere = sphere(pos=vector(self._worldPos,0,0),color=color.white, texture=Texture, radius=self._radius, make_trail=True, interval=5, retain=500)

    def gravitationalAttraction(self, attractor):
        self._force = Gravity * (attractor._mass * self._mass)/self._distance**2
        
    def angularVelocity(self):
        self._angularVelocity = math.sqrt((self._force)/(self._mass * self._distance))
        
    def angularPosition(self, t):
        # initail theta position
        initialTheta = 0
        self._theta = initialTheta + self._angularVelocity * t
        return self._theta

    def update(self,t,dt,attractor):
        self.gravitationalAttraction(attractor)
        self.angularVelocity()
        self._position = self.angularPosition(t+dt) - self.angularPosition(t)
        if(self._moon):
            self._v = vector(self._worldPos - attractor._worldPos,0,0)
            self._v = rotate(self._v, angle = self._position, axis=vector(0,1,0))
            self._sphere.pos = attractor._sphere.pos + self._v
        else:
            self._sphere.pos = rotate(self._sphere.pos, angle = self._position, axis=vector(0,1,0))
        
