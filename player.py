from OpenGL.GL import *
from OpenGL.GLU import *

import glm
from enum import Enum

import math
from math import radians

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
        self.dir = glm.vec3(0, 0, -1)   # TODO replace with 3rd column of modelview matrix
        self.speed = 0.25

        self.axis = glm.vec3(0.0, 0.0, 0.0)
        self.mat = glm.mat3()

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


    # Moves the cube by a specified shift amount
    def translate_view(self, shift):
        glTranslate(shift.x, shift.y, shift.z)


    def rotate_h(self, delta):
        # Shift the camera to the origin
        shift = glm.vec3(self.loc.x, self.loc.y, self.loc.z)
        self.translate_view(shift)

        # Get the modelview matrix
        m = glGetFloatv(GL_MODELVIEW_MATRIX)

        u = glm.normalize(glm.vec3(float(m[0][0]), float(m[0][1]), float(m[0][2])))
        v = glm.normalize(glm.vec3(float(m[1][0]), float(m[1][1]), float(m[1][2])))
        w = glm.normalize(glm.vec3(float(m[2][0]), float(m[2][1]), float(m[2][2])))

        R = glm.mat3(
                u[0],  u[1],  u[2],
                v[0],  v[1],  v[2],
               -w[0], -w[1], -w[2]
                )
        self.mat = R
        R_inv = glm.inverse(R)

        # Rotate the camera around the horizontal axis
        deg_y = 0.3*delta
#        axis_h = right
        ref = glm.vec3(1.0, 0.0, 0.0)
        axis_h = R*ref
#        axis_h = (axis_h[0], 0.0, axis_h[)
        self.axis = axis_h
        glRotate(deg_y, axis_h.x, axis_h.y, axis_h.z)

        # Get the modelview matrix TODO DELETE
        m = glGetFloatv(GL_MODELVIEW_MATRIX)
        right   = glm.normalize(glm.vec3(float(m[0][0]), float(m[0][1]), float(m[0][2])))
        up      = glm.normalize(glm.vec3(float(m[1][0]), float(m[1][1]), float(m[1][2])))
        forward = glm.normalize(glm.vec3(float(m[2][0]), float(m[2][1]), float(m[2][2])))

        R = glm.mat3(
                right[0],   right[1],   right[2],
                up[0],      up[1],      up[2],
               -forward[0],-forward[1],-forward[2]
                )
        self.mat = R


        # Shift back to the player position
        shift = glm.vec3(-self.loc.x, -self.loc.y, -self.loc.z)
        self.translate_view(shift)


    def rotate_v(self, delta):
        # Shift the camera to the origin
        shift = glm.vec3(self.loc.x, self.loc.y, self.loc.z)
        self.translate_view(shift)

        # Rotate the camera around the vertical axis
        deg_x = 0.3*delta
        axis_v = glm.vec3(0.0, 1.0, 0.0)
        glRotate(deg_x, axis_v.x, axis_v.y, axis_v.z)



        # Get the modelview matrix TODO DELETE
        m = glGetFloatv(GL_MODELVIEW_MATRIX)
        right   = glm.normalize(glm.vec3(float(m[0][0]), float(m[0][1]), float(m[0][2])))
        up      = glm.normalize(glm.vec3(float(m[1][0]), float(m[1][1]), float(m[1][2])))
        forward = glm.normalize(glm.vec3(float(m[2][0]), float(m[2][1]), float(m[2][2])))

        B = glm.mat3(
                right[0],   right[1],   right[2],
                up[0],      up[1],      up[2],
               -forward[0],-forward[1],-forward[2]
                )
        self.mat = B



        # Shift back to the player position
        shift = glm.vec3(-self.loc.x, -self.loc.y, -self.loc.z)
        self.translate_view(shift)


    # Changes the view of the player
    def rotate_view(self, delta_x, delta_y):
        if delta_x != 0:
            self.rotate_v(delta_x)

        if delta_y != 0: 
            self.rotate_h(delta_y)


    def jump(self):
        # TODO Implement
        pass


    def get_loc(self):
        return (self.loc.x, self.loc.y, self.loc.z)


    def get_vel(self):
        return (self.vel.x, self.vel.y, self.vel.z)


    # Update player status
    def update(self):
        # Construct local basis vectors
        m = glGetFloatv(GL_MODELVIEW_MATRIX)
        right   = glm.normalize(glm.vec3(float(m[0][0]), float(m[0][1]), float(m[0][2])))
        up      = glm.normalize(glm.vec3(float(m[1][0]), float(m[1][1]), float(m[1][2])))
        forward = glm.normalize(glm.vec3(float(m[2][0]), float(m[2][1]), float(m[2][2])))
        print("Right:             (" + str(right.x)   + ",\t " + str(right.y)   + ",\t " + str(right.z)   + ")")
        print("Up:                (" + str(up.x)      + ",\t " + str(up.y)      + ",\t " + str(up.z)      + ")")
        print("Forward:           (" + str(forward.x) + ",\t " + str(forward.y) + ",\t " + str(forward.z) + ")")

        vx = (self.vel.x * right.x) + (self.vel.y * up.x) - (self.vel.z * forward.x)
#        vy = (self.vel.x * right.y) + (self.vel.y * up.y) - (self.vel.z * forward.y)
        vy = 0
        vz = (self.vel.x * right.z) + (self.vel.y * up.z) - (self.vel.z * forward.z)

#        print("--Local vel: (" + str(vx) + ", " + str(vy) + ", " + str(vz) + ")")
        glTranslate(-vx, -vy, -vz)
#        glTranslate(-vx, 0, -vz)

        self.loc.x += vx
        self.loc.y += vy
        self.loc.z += vz
#        print(self.loc.x, self.loc.y, self.loc.z)
        print("Rotation axis (h): (" + str(self.axis.x) + ",\t " + str(self.axis.y) + ",\t " + str(self.axis.z) + ")")
        print(self.mat)
        print()
