from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

class Window():
    def __init__(self, width, height, offset_z=10):
        self.width = width
        self.height = height
        self._setup(width, height, offset_z)

    # Creates the pygame environment
    @staticmethod
    def _setup(width, height, offset_z=10):
        # Initialize pygame and create the window
        pygame.init()
        pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

        # Set the background color
        glClearColor(0.5, 0.5, 0.5, 1)

        # Enable drawing properties
        glEnable(GL_LINE_SMOOTH)
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_CULL_FACE)
        glDepthFunc(GL_LEQUAL)

        # Set field of view (degrees, aspect ratio, clipping planes)
        gluPerspective(45, float(width)/float(height), 0.1, 50.0)

        # Translate the environment
        glTranslatef(0, 0, -offset_z)


    # Closes the pygame environment
    @staticmethod
    def close():
        pygame.quit()
        quit()
