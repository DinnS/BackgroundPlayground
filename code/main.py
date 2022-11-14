import sys
import pygame

from settings import *
from background import Background
from day_time import Day_time
from ui import UI

class Game:
    def __init__(self):
        # Game setup
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),pygame.FULLSCREEN)
        pygame.display.set_caption('Background')
        self.clock = pygame.time.Clock()

        # Own class init
        self.day_time = Day_time()
        self.start_day_time = self.day_time.update()

        self.ui = UI(self.screen, self.day_time)

        self.background = Background(self.screen,self.start_day_time)


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

            # Day time setup
            self.current_day_time = self.day_time.update()

            # Background setup
            self.background.run(self.current_day_time)

            # Day menu setup
            self.ui.run(self.current_day_time)

            # Update screen
            pygame.display.flip()
            self.clock.tick(60)

if __name__ == '__main__':
    game = Game()
    game.run()