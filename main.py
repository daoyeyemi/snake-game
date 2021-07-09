import pygame
import time
# module that contains constants frequently used in pygame
from pygame.locals import *

if __name__ == "__main__":
    pygame.init()
    # initialize window / screen for display
    surface = pygame.display.set_mode((1000, 500))
    # color
    surface.fill((200, 125, 5))
    # update the full display surface to the screen
    pygame.display.flip()

    running = True

    while running == True: 
        # get events from queue
        for event in pygame.event.get():
            # if key is clicked
            if event.type == KEYDOWN:
                # if key happens to be escape key
                if event.key == K_ESCAPE:
                    running = False
            # exit button is clicked on module
            elif event.type == QUIT:
                running = False