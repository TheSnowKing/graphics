import pygame
from pygame.locals import *

from player import Direction

class EventHandler():
    # Constructor
    def __init__(self, window, player):
        self.player = player
        self.window = window
        pass

    # Main event handler
#    def handle_event(self, event):
    def handle_events(self):
        mouse = pygame.mouse.get_pos()
        moved = pygame.mouse.get_rel()
        pressed = pygame.mouse.get_pressed()

        if pressed[2]:
            self.player.rotate_view(moved[0], moved[1])

        amnt = 15
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            self.player.rotate_view(amnt, 0)
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            self.player.rotate_view(-amnt, 0)
        if pygame.key.get_pressed()[pygame.K_UP]:
            self.player.rotate_view(0, -amnt)
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            self.player.rotate_view(0, amnt)



        for event in pygame.event.get():
            # Check for user exit
            if event.type == pygame.QUIT:
                self.window.close()

            # Check if key is pressed
            if event.type == pygame.KEYDOWN:
                self._key_down(event)

            # Check if key is released
            if event.type == pygame.KEYUP:
                self._key_up(event)



    # Helper method for keydown
    def _key_down(self, event):
        if event.key == pygame.K_p:
            # TODO Implement pause
            pass


        # WASD movement
        if event.key == pygame.K_w:
            self.player.start_motion(Direction.IN)
        if event.key == pygame.K_s:
            self.player.start_motion(Direction.OUT)
        if event.key == pygame.K_a:
            self.player.start_motion(Direction.LEFT)
        if event.key == pygame.K_d:
            self.player.start_motion(Direction.RIGHT)


        # Left and right keys
        if event.key == pygame.K_LEFT:
#            self.player.rotate_view(-5, 0)
            pass
        if event.key == pygame.K_RIGHT:
#            self.player.rotate_view(5, 0)
            pass

        # Up and down keys
        if event.key == pygame.K_UP:
#            self.player.start_motion(Direction.UP)
            pass
        if event.key == pygame.K_DOWN:
#            self.player.start_motion(Direction.DOWN)
            pass

        # In and out keys
        if event.key == pygame.K_x:
            self.player.start_motion(Direction.IN)
        if event.key == pygame.K_z:
            self.player.start_motion(Direction.OUT)


    # Helper method for keyup
    def _key_up(self, event):

        # WASD movement
        if event.key == pygame.K_w:
            self.player.stop_motion(Direction.IN)
        if event.key == pygame.K_s:
            self.player.stop_motion(Direction.OUT)
        if event.key == pygame.K_a:
            self.player.stop_motion(Direction.LEFT)
        if event.key == pygame.K_d:
            self.player.stop_motion(Direction.RIGHT)


        # Left and right keys
        if event.key == pygame.K_LEFT:
#            self.player.stop_motion(Direction.LEFT)
            pass
        if event.key == pygame.K_RIGHT:
#            self.player.stop_motion(Direction.RIGHT)
            pass

        # Up and down keys 
        if event.key == pygame.K_UP:
#            self.player.stop_motion(Direction.UP)
            pass
        if event.key == pygame.K_DOWN:
#            self.player.stop_motion(Direction.DOWN)
            pass

        # In and out keys
        if event.key == pygame.K_x:
            self.player.stop_motion(Direction.IN)
        if event.key == pygame.K_z:
            self.player.stop_motion(Direction.OUT)

