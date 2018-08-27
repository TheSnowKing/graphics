from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

import math
from shapes import Cube, colors
from player import Player
from event import EventHandler
from window import Window

def ground():
    ground_height = 0.2
    ground_vertices = (
                (30, -ground_height, 50),
                (30, -ground_height, -50),
                (-30, -ground_height, -50),
                (-30, -ground_height, 50)
                )
    glBegin(GL_QUADS)
    color = (0.30, 0.30, 0.30)
    glColor3fv(color)
    for vertex in ground_vertices:
        glVertex3fv(vertex)
    glEnd()

# Main program
def main():
    offset_z = 20.0

    # Instantiate game components
#    window = Window(800, 600, offset_z)
    window = Window(1918, 1000, offset_z)
    player = Player((0,0,offset_z))
    event_handler = EventHandler(window, player)

    done = False    # For game loop

    color = colors[3]
    counter = 0             # Counter for sinusoidal oscillations and color flicker

    # Create the dictionary of cubes
    num_cubes = 3
    cube_dict = {}
    for index in range(num_cubes):
        cube = Cube(Cube.unit_cube(), color, True)

        shift = (2*index-2, 0.5, 0)
        cube.move(shift)

        cube.reset_pivot()         # Set the pivot to be the cube's center
        cube_dict[index] = cube     # Add cube to the dictionary

    cube_1 = Cube(Cube.unit_cube(), color, True)
    shift = (0.0, 10.0, offset_z)
    cube_1.move(shift)
    cube_dict[3] = cube_1

    cube_2 = Cube(Cube.unit_cube(), color, True)
    shift = (10.0, 0.0, offset_z)
    cube_2.move(shift)
    cube_dict[4] = cube_2

    cube_3 = Cube(Cube.unit_cube(), color, True)
    shift = (-10.0, 0.0, offset_z)
    cube_3.move(shift)
    cube_dict[5] = cube_3

    cube_4 = Cube(Cube.unit_cube(), color, True)
    shift = (0.0, 0.0, offset_z + 10.0)
    cube_4.move(shift)
    cube_dict[6] = cube_4

#    glTranslate(player.get_loc()[0], player.get_loc()[1], player.get_loc()[2])

    # Game loop
    while not done:
#        for event in pygame.event.get():
#            event_handler.handle_event(event)
        event_handler.handle_events()


        # Clear the slate between frames before drawing
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        # Translate the camera according to the player's velocity
        player.update()

        # Draw the ground
        ground()
        # Draw each of the cubes
        for key in cube_dict:
            cube = cube_dict[key]

#            pivot = cube.pivot
#            new_loc = (cube.pivot[0] + math.sin(0.1*counter), cube.get_center()[1], cube.get_center()[2])
#            cube.set_loc(new_loc)
#            cube.reset_pivot()
#            cube.rotate(5,1,1,1)
#            cube.set_pivot(pivot)
            cube.draw()

#        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()



#        print(mouse)
#        print(click)
#        print()
        pygame.display.flip()
        pygame.time.wait(10)

        counter += 1

# ********************
# Run the main program
# ********************
main()

