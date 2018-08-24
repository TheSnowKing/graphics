from OpenGL.GL import *
from OpenGL.GLU import *

from math import sin, cos, radians
import glm

edges = (
    (0, 1),
    (0, 2),
    (0, 4),
    (1, 3),
    (1, 5),
    (2, 3),
    (2, 6),
    (3, 7),
    (4, 5),
    (4, 6),
    (5, 7),
    (6, 7)
    )

surfaces = (
    (0, 1, 3, 2),
    (0, 4, 5, 1),
    (0, 2, 6, 4),
    (1, 5, 7, 3),
    (2, 3, 7, 6),
    (4, 6, 7, 5)
    )

colors = (
    (0, 0, 0),
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
    )


class Cube():

    # Returns a list of vertices for the unit cube
    @staticmethod
    def unit_cube():
        vertices = [
            [0, 0, 0],
            [0, 0, 1],
            [0, 1, 0],
            [0, 1, 1],
            [1, 0, 0],
            [1, 0, 1],
            [1, 1, 0],
            [1, 1, 1]
            ]
        return vertices


    # Constructor TODO Add initial location as an input param
    def __init__(self, vertices, color=(0,0,0), reposition=False):
        self.vertices = vertices
        self.color = color

        # Reposition all vertices so that the center of the cube
        # resides at the origin of the world
        if reposition:
            center = self.get_center()
            shift = (-center[0], -center[1], -center[2])
            self.move(shift)

        # Set the pivot point
        self.pivot = self.get_center()


    # Provides a string output of the cube
    def __str__(self):
        return "Center: " + str(self.get_center()) + "\tpivot: " + str(self.pivot)


    # Sets the color of the cube
    def set_color(self, color):
        self.color = color


    # Calculates the center of the cube
    def get_center(self):
        xc = 0
        yc = 0
        zc = 0

        # Compute the average location of vertices
        for vertex in self.vertices:
            xc += vertex[0]
            yc += vertex[1]
            zc += vertex[2]
        xc /= len(self.vertices)
        yc /= len(self.vertices)
        zc /= len(self.vertices)
        return (xc, yc, zc)


    # Sets the pivot to a 3-tuple
    def set_pivot(self, pivot):
        self.pivot = pivot


    # Resets the pivot to the center of the cube
    def reset_pivot(self):
        self.pivot = self.get_center()


    # Moves the cube by a specified shift amount
    def move(self, shift):
        for vertex in self.vertices:
            vertex[0] += shift[0]
            vertex[1] += shift[1]
            vertex[2] += shift[2]


    # Sets the cube to a new location
    def set_loc(self, new_loc):
        center = self.get_center()

        # Calculate the difference between the new location
        # and the cube's current center
        x_change = new_loc[0] - center[0]
        y_change = new_loc[1] - center[1]
        z_change = new_loc[2] - center[2]

        # Move the cube to the new location
        shift = (x_change, y_change, z_change)
        self.move(shift)


    # Scales the cube by a specified scale factor
    def scale(self, factor):
        if factor > 0:
            center = self.get_center()
            half_length = abs(self.vertices[0][2] - self.vertices[1][2])/2

            for vertex in self.vertices:
                if vertex[0] < center[0]:
                    vertex[0] -= half_length * (factor - 1)
                else:
                    vertex[0] += half_length * (factor - 1)

                if vertex[1] < center[1]:
                    vertex[1] -= half_length * (factor - 1)
                else:
                    vertex[1] += half_length * (factor - 1)

                if vertex[2] < center[2]:
                    vertex[2] -= half_length * (factor - 1)
                else:
                    vertex[2] += half_length * (factor - 1)


    # Rotates the cube about the pivot, using a rotational axis
    # defined by the directional vector (x, y, z)
    def rotate(self, deg, x, y, z):
        # Shift the cube so that it's pivot resides at the origin
        shift = (-self.pivot[0], -self.pivot[1], -self.pivot[2])
        self.move(shift)

        # Create a vec3 using the components of the orientation vector
        axis = glm.vec3(x, y, z)

        a = radians(deg)
        c = cos(a)
        s = sin(a)
        m = glm.mat4(1.0)   # Identity matrix

        # Construct the rotation matrix using the identity
        m = glm.rotate(m, a, axis)

        # Rotate each of the vertices
        for vertex in self.vertices:
            # Perform the rotation
            v = glm.vec4(vertex[0], vertex[1], vertex[2], 1)
            v = m*v

            # Update the location of the vertices
            vertex[0] = v[0]
            vertex[1] = v[1]
            vertex[2] = v[2]

        # Move the cube back and its pivot back to the original location
        shift = (-shift[0], -shift[1], -shift[2])
        self.move(shift)


    # Draws the wireframe mesh of the cube
    def draw_mesh(self, color=(1,1,1)):
        glBegin(GL_LINES)
        glColor(color)

        for edge in edges:
            for vertex in edge:
                glVertex3fv(self.vertices[vertex])
        glEnd()


    # Draws the faces of the cube
    def draw(self):
        glBegin(GL_QUADS)
        glColor(self.color)

        # Draw the faces of the cube 
        for surface in surfaces:
            for vertex in surface:
                glVertex3fv(self.vertices[vertex])
        glEnd()

        # Draw the frame of the cube
        black = colors[0]
        if self.color is black:
            self.draw_mesh((1,1,1)) # Use a white mesh
        else:
            self.draw_mesh((0,0,0)) # Use a black mesh

