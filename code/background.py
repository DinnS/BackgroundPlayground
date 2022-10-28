import pygame
import random

from settings import *
from support import import_name_sprite

class Background:
    def __init__(self,screen):
        self.display = screen

        # Elements background

        # light cloud
        self.cloud_light_sprite = pygame.sprite.Group()
        self.cloud_light_amount = 30
        self.spawn_random_position_sprite(self.cloud_light_sprite,'../graphics/light_cloud', CloudLight, self.cloud_light_amount)

        # dark cloud
        self.cloud_dark_sprite = pygame.sprite.Group()
        self.cloud_dark_amount = 20
        self.spawn_random_position_sprite(self.cloud_dark_sprite,'../graphics/dark_cloud',CloudDark, self.cloud_dark_amount)


    # Spawn object functions
    def spawn_random_position_sprite(self,sprite,sprite_path,sprite_class,sprite_amount_spawn):
        # The array in which each sprite is located
        sprite_list = import_name_sprite(sprite_path)
        # Number of sprites
        sprite_variability = len(sprite_list)

        # Random spawn sprites
        for _ in range(sprite_amount_spawn):
            # Position spawn
            spawn_position_x = random.randrange(0, SCREEN_WIDTH)
            spawn_position_y = random.randrange(0, SCREEN_HEIGHT)

            # Number of the displayed sprite
            sprite_display = random.randrange(0,sprite_variability)
            # Create and add sprite to background list
            new_sprite = sprite_class(sprite_list[sprite_display], spawn_position_x,spawn_position_y)
            sprite.add(new_sprite)

    def spawn_new_sprite(self,sprite,sprite_path,sprite_class):
        # The array in which each sprite is located
        sprite_list = import_name_sprite(sprite_path)
        # Number of sprites
        sprite_variability = len(sprite_list)

        sprite_number = random.randrange(0,sprite_variability)

        new_sprite = sprite_class(sprite_list[sprite_number], 0, random.randrange(0, SCREEN_HEIGHT))
        sprite.add(new_sprite)

    # Draw objects
    def cloud_light(self):
        if len(self.cloud_light_sprite) < self.cloud_light_amount:
            self.spawn_new_sprite(self.cloud_light_sprite,'../graphics/light_cloud',CloudLight)

        self.cloud_light_sprite.draw(self.display)
        self.cloud_light_sprite.update()

    def cloud_dark(self):
        if len(self.cloud_dark_sprite) < self.cloud_dark_amount:
            self.spawn_new_sprite(self.cloud_dark_sprite,'../graphics/dark_cloud',CloudDark)

        self.cloud_dark_sprite.draw(self.display)
        self.cloud_dark_sprite.update()

    def run(self):
        self.cloud_dark()
        self.cloud_light()



# General setting of background sprites

class Sprite(pygame.sprite.Sprite):
    def __init__(self, sprite_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]

        # Permission to decimal movement
        self.pos_x = pos_x
        self.pos_y = pos_y

        self.count = 0
    def check_sprite_status(self):
        if self.rect.left > SCREEN_WIDTH:
            self.kill()


# Classes of background elements

class CloudLight(Sprite):
    def __init__(self, sprite_path, pos_x, pos_y):
        super().__init__(sprite_path, pos_x, pos_y)

    def update(self):
        self.check_sprite_status()
        self.rect.center = [self.pos_x,self.pos_y]
        self.pos_x += 1


class CloudDark(Sprite):
    def __init__(self, sprite_path, pos_x, pos_y):
        super().__init__(sprite_path, pos_x, pos_y)

    def update(self):
        self.check_sprite_status()
        self.rect.center = [self.pos_x,self.pos_y]
        self.pos_x += 0.5






