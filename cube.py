
from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *
from shapes import Cube, colors

import random

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


def setup(width, height, offset_z=10):
    pygame.init()
    pygame.display.set_mode((width, height), DOUBLEBUF | OPENGL)

    # Set field of view (degrees, aspect ratio, clipping planes)
    gluPerspective(45, float(width)/float(height), 0.1, 50.0)

    # (x,y,z) for translating the object in space.
    # This is so the camera doesn't end up inside the cube
    glTranslatef(0, 0, -offset_z)


def close():
    pygame.quit()
    quit()


def main():
    offset_z = 12.0
    setup(800, 600, offset_z)

    left_pressed = False    # Toggle to True if the left arrow-key is pressed down
    right_pressed = False   # Toggle to True if the right arrow-key is pressed down
    up_pressed = False      # Toggle to True if the up arrow-key is pressed down
    down_pressed = False    # Toggle to True if the down arrow-key is pressed down 

    collided = False
    paused = False
    mousewheel_enabled = True

    color = colors[5]
    counter = 0             # Counter for sinusoidal oscillations and color flicker

    # Create the dictionary of cubes
    num_cubes = 2
    cube_dict = {}
    for index in range(num_cubes):
        cube = Cube(unit_cube(), color, True)

        shift = (2*index, 0, 0)
        cube.move(shift)

        cube.reset_pivot()         # Set the pivot to be the cube's center
        cube_dict[index] = cube     # Add cube to the dictionary


    # Game loop
    while not collided:

        for event in pygame.event.get():
            # Check for user exit
            if event.type == pygame.QUIT:
                close()

            # Check if key is pressed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    paused = True

                # Left and right keys
                if event.key == pygame.K_LEFT:
                    left_pressed = True
                if event.key == pygame.K_RIGHT:
                    right_pressed = True

                # Up and down keys
                if event.key == pygame.K_UP:
                    up_pressed = True
                if event.key == pygame.K_DOWN:
                    down_pressed = True

            # Check if key is released
            if event.type == pygame.KEYUP:

                # Left and right keys
                if (event.key == pygame.K_LEFT) and (left_pressed == True): 
                    left_pressed = False
                if (event.key == pygame.K_RIGHT) and (right_pressed == True):
                    right_pressed = False

                # Up and down keys 
                if (event.key == pygame.K_UP) and (up_pressed == True): 
                    up_pressed = False
                if (event.key == pygame.K_DOWN) and (down_pressed == True):
                    down_pressed = False

            # Check for mousewheel movement.
            # Movement is along the world z-axis (semi-zoom)
            if mousewheel_enabled:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 4:
                        glTranslatef(0, 0, 0.5)
                    if event.button == 5:
                        glTranslate(0, 0, -0.5)



        # Clear the slate between frames before drawing
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

#        cur_color = colors[counter % len(colors)]
        for key in cube_dict:
            cube = cube_dict[key]
#            new_loc = (cube.pivot[0] + sin(counter), cube.get_center()[1], cube.get_center()[2])
#            cube.set_loc(new_loc)
            cube.rotate(5,1,1,1)
#            cube.set_color(cur_color)
            cube.draw()

        pygame.display.flip()
        pygame.time.wait(10)    # Wait 10 milliseconds

        counter += 1


main()
