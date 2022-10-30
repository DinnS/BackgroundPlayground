import sys
import pygame

from settings import *
from background import Background

class Game:
    def __init__(self):
        # Game setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
        pygame.display.set_caption('Background')
        self.clock = pygame.time.Clock()

        # Class init
        self.background = Background(self.screen)


    def close_game(self):
        pygame.quit()
        sys.exit()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.close_game()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.close_game()


            # Background setup
            self.background.run()

            # Update screen
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()