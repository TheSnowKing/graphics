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
    def handle_event(self, event):
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

        # Left and right keys
        if event.key == pygame.K_LEFT:
            self.player.start_motion(Direction.LEFT)
        if event.key == pygame.K_RIGHT:
            self.player.start_motion(Direction.RIGHT)

        # Up and down keys
        if event.key == pygame.K_UP:
            self.player.start_motion(Direction.UP)
        if event.key == pygame.K_DOWN:
            self.player.start_motion(Direction.DOWN)

        # In and out keys
        if event.key == pygame.K_x:
            self.player.start_motion(Direction.IN)
        if event.key == pygame.K_z:
            self.player.start_motion(Direction.OUT)


    # Helper method for keyup
    def _key_up(self, event):
        # Left and right keys
        if event.key == pygame.K_LEFT:
            self.player.stop_motion(Direction.LEFT)
        if event.key == pygame.K_RIGHT:
            self.player.stop_motion(Direction.RIGHT)

        # Up and down keys 
        if event.key == pygame.K_UP:
            self.player.stop_motion(Direction.UP)
        if event.key == pygame.K_DOWN:
            self.player.stop_motion(Direction.DOWN)

        # In and out keys
        if event.key == pygame.K_x:
            self.player.stop_motion(Direction.IN)
        if event.key == pygame.K_z:
            self.player.stop_motion(Direction.OUT)

