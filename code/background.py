import pygame
import random

from settings import *
from support import import_sprite

class Background:
    def __init__(self,screen):
        self.display = screen
        self.sprite = pygame.sprite.Group()

        # Spawn clouds
        self.spawn_sprite_random_position('../graphics/light_cloud',CloudLight)
        self.spawn_sprite_random_position('../graphics/dark_cloud',CloudDark)


    def spawn_sprite_random_position(self,sprite_path,sprite_class):
        # The array in which each sprite is located
        sprite_list = import_sprite(sprite_path)
        # Number of sprites
        sprite_variability = len(sprite_list)

        # Random spawn sprites
        for sprite_number in range(sprite_variability):
            new_sprite = sprite_class(sprite_list[sprite_number], random.randrange(0, SCREEN_WIDTH),random.randrange(0, SCREEN_HEIGHT))
            self.sprite.add(new_sprite)

    def run(self):
        self.sprite.draw(self.display)
        self.sprite.update()


# General setting of background elements

class Sprite(pygame.sprite.Sprite):
    def __init__(self, sprite_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        # Permission to decimal movement
        self.pos_x = pos_x
        self.pos_y = pos_y


# Classes of background elements

class CloudLight(Sprite):
    def __init__(self, sprite_path, pos_x, pos_y):
        super().__init__(sprite_path, pos_x, pos_y)

    def update(self):
        self.rect.center = [self.pos_x,self.pos_y]
        self.pos_x += 1


class CloudDark(Sprite):
    def __init__(self, sprite_path, pos_x, pos_y):
        super().__init__(sprite_path, pos_x, pos_y)

    def update(self):
        self.rect.center = [self.pos_x,self.pos_y]
        self.pos_x += 0.5






