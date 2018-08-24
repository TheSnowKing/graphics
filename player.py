import glm
from enum import Enum

class Direction(Enum):
    LEFT = 1
    RIGHT = 2
    UP = 3
    DOWN = 4
    IN = 5
    OUT = 6


class Player():

    # Constructor
    def __init__(self, loc=(0,0,0)):
        self.loc = glm.vec3(loc[0], loc[1], loc[2])
        self.vel = glm.vec3(0, 0, 0)
        self.acc = glm.vec3(0, 0, 0)
        self.dir = glm.vec3(0, 0, -1)

        self.force = glm.vec3(0, 0, 0)

        self.mass = 4
        self.coef = 0.5 # Coefficent of kinetic friction
        self.speed = 0.3


    # Output representation
    def __str__(self):
        return str(self.loc) + "\n" + str(self.vel) + "\n" + str(self.acc)


    # Begin moving in a specified direction
    def start_motion(self, direction):

        if direction is Direction.LEFT:
            self.vel.x -= self.speed
        elif direction is Direction.RIGHT:
            self.vel.x += self.speed

        if direction is Direction.UP:
            self.vel.y += self.speed
        elif direction is Direction.DOWN:
            self.vel.y -= self.speed

        if direction is Direction.IN:
            self.vel.z -= self.speed
        elif direction is Direction.OUT:
            self.vel.z += self.speed

    # Stop moving in a specified direction
    def stop_motion(self, direction):

        if direction is Direction.LEFT:
            self.vel.x += self.speed
        elif direction is Direction.RIGHT:
            self.vel.x -= self.speed

        if direction is Direction.UP:
            self.vel.y -= self.speed
        elif direction is Direction.DOWN:
            self.vel.y += self.speed

        if direction is Direction.IN:
            self.vel.z += self.speed
        elif direction is Direction.OUT:
            self.vel.z -= self.speed


    def get_loc(self):
        return (self.loc.x, self.loc.y, self.loc.z)


    def get_vel(self):
        return (self.vel.x, self.vel.y, self.vel.z)


    # Sets the net force acing on the player
    # Input should be a 3-tuple
    def set_force(self, force):
        self.force.x = force[0]
#        self.force.y = force[1]
#        self.force.z = force[2]



    def _calculate_friction(self):
        friction = glm.vec3()
        friction.x = -self.coef * self.vel.x
        friction.y = -self.coef * self.vel.y 
        friction.z = -self.coef * self.vel.z
        return friction

    # Update player status
    def update(self):
#        friction = self._calculate_friction()
#        self.force.x += friction.x
#        self.force.y += friction.y
#        self.force.z += friction.z

#        self.acc.x = self.force.x/self.mass
#        self.acc.y = self.force.y/self.mass
#        self.acc.z = self.force.z/self.mass

        self.vel.x += self.acc.x
        self.vel.y += self.acc.y
        self.vel.z += self.acc.z

        self.loc.x += self.vel.x
        self.loc.y += self.vel.y
        self.loc.z += self.vel.z
