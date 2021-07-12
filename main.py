import pygame
import time
# module that contains constants frequently used in pygame
from pygame.locals import *

class Snake:
    def __init__(self, parent_screen):
        self.parent_screen = parent_screen
        self.block = pygame.image.load('resources/block.jpeg').convert()
        # draw image onto another
        self.xblock = 100
        self.yblock = 100
        self.direction = 'down'
    
    def draw(self):
        self.parent_screen.fill((200, 125, 5))
        # draw one image onto another
        self.parent_screen.blit(self.block, (self.xblock, self.yblock))
         # update the full display surface to the screen
        pygame.display.flip()
    
    def move_left(self):
        self.direction == 'left'

    def move_right(self):
        self.direction == 'right'

    def move_up(self):
        self.direction == 'up'

    def move_down(self):
        self.direction == 'down'

    def walk(self):
        
        if self.direction == 'up':
            self.yblock -= 10
        if self.direction == 'down':
            self.yblock += 10
        if self.direction == 'left':
            self.xblock -= 10
        if self.direction == 'right':
            self.xblock += 10
            
        self.draw()

class Game:
    def __init__(self):
        pygame.init()
        # initialize window / screen for display
        self.surface = pygame.display.set_mode((500, 500))
        # color
        self.surface.fill((200, 125, 5))
        self.snake = Snake(self.surface)
        self.snake.draw()

    def run(self):
        running = True

        while running == True: 
            # pygame.event.get() will 
            # get events from queue and will start game
            for event in pygame.event.get():
                # if key is clicked
                if event.type == KEYDOWN:
                    # if key happens to be escape key
                    if event.key == K_ESCAPE:
                        running = False

                    if event.key == K_UP:
                        self.snake.move_up()
                    if event.key == K_DOWN:
                        self.snake.move_down()
                    if event.key == K_RIGHT:
                        self.snake.move_right()
                    if event.key == K_LEFT:
                        self.snake.move_left()
                # exit button is clicked on module
                elif event.type == QUIT:
                    running = False

            self.snake.walk()
            time.sleep(0.2)

if __name__ == "__main__":
    game = Game()

    game.run()