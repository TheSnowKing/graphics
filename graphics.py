import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


vertices = (
    (0, 0, 0),
    (0, 0, 1)
    (0, 0, 1),
    (0, 1, 0),
    (0, 1, 1),
    (1, 0, 0),
    (1, 0, 1),
    (1, 1, 0),
    (1, 1, 1)
    )

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

faces = (
    (0, 1, 2, 3),
    (0, 1, 5, 4),
    (0, 2, 6, 4),
    (1, 3, 7, 5),
    (2, 3, 7, 6),
    (4, 5, 7, 6)
    )

#def cube():

class Cube:
    def __init__(self, vertices):
        
            

class Spam:
    total_cost = 0
    items_count = 0

    def __init__(self, name, cost):
        self._name = name
        self._cost = cost
        self.__class__.total_cost += cost
        self.__class__.items_count += 1

    def name(self, name):
        self._name = name 

    def get_name(self):
        return self._name

    def cost(self, cost):
        self.__class__.total_cost = self.__class__.total_cost - self._cost + cost
        self._cost = cost

    def get_cost(self):
        return self._cost

    @classmethod
    def get_total_cost(cls):
        return cls.total_cost

    @classmethod
    def get_items_count(cls):
        return cls.items_count



def setup(width, height):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    gluPerspective(45, width/height, 0.1, 50.0)
    glTranslatef(0, 0, 0, -5)


def close():
    pygame.quit()
    quit()


def main():
    setup(800, 600)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close()

    # Clear the slate between frames before drawing
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#    cube()
    pygame.display.flip()
    pygame.time.wait(10)    # Wait 10 milliseconds

main()
