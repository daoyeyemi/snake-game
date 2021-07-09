import pygame
import time
# module that contains constants frequently used in pygame
from pygame.locals import *

class Game:
    def __init__(self):
        pass

    def run(self):
        pass
    
if __name__ == "__main__":
    game = Game()

    game.run()

    pygame.init()
    # initialize window / screen for display
    surface = pygame.display.set_mode((1000, 500))
    # color
    surface.fill((200, 125, 5))
    
    block = pygame.image.load('resources/block.jpeg').convert()
    # draw image onto another
    xblock = 100
    yblock = 100

    surface.blit(block, (xblock, yblock))
    # update the full display surface to the screen
    pygame.display.flip()

    def draw_block():
        surface.fill((200, 125, 5))

        surface.blit(block, (xblock, yblock))
        
        pygame.display.flip()

    running = True

    while running == True: 
        # pygame.event.get() will 
        # get events from queue
        for event in pygame.event.get():
            # if key is clicked
            if event.type == KEYDOWN:
                # if key happens to be escape key
                if event.key == K_ESCAPE:
                    running = False

                if event.key == K_UP:
                    yblock = yblock - 10
                    draw_block()
                if event.key == K_DOWN:
                    yblock = yblock + 10
                    draw_block()
                if event.key == K_RIGHT:
                    xblock = xblock + 10
                    draw_block()
                if event.key == K_LEFT:
                    xblock = xblock - 10
                    draw_block()
            # exit button is clicked on module
            elif event.type == QUIT:
                running = False


