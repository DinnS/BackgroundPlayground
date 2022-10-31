import pygame
import random

from settings import *
from support import import_name_sprite
from day_time import Day_time


class Background:
    def __init__(self,screen):
        self.display = screen

        # Setup day time and start day period
        self.day_time = Day_time()
        self.game_time = self.day_time.update()

        self.day_period = self.check_time_period(self.game_time)
        self.path_image = '../graphics/' + self.day_period

        # Background
        self.background_image = pygame.image.load(self.path_image + 'background/background.png')
        self.background_image = pygame.transform.scale(self.background_image,(SCREEN_WIDTH,SCREEN_HEIGHT))
        # Elements background

        # light cloud
        self.cloud_light_sprite = pygame.sprite.Group()
        self.cloud_light_amount = 30
        self.spawn_random_position_sprite(self.cloud_light_sprite,self.path_image + 'cloud-light', CloudLight, self.cloud_light_amount)

        # dark cloud
        self.cloud_dark_sprite = pygame.sprite.Group()
        self.cloud_dark_amount = 20
        self.spawn_random_position_sprite(self.cloud_dark_sprite,self.path_image + 'cloud-dark',CloudDark, self.cloud_dark_amount)

    def test(self):
        self.cloud_light_amount = 10

    def check_time_period(self,game_time):
        self.game_time_hours = int(game_time.split(':')[0])

        if self.game_time_hours >= 6 and self.game_time_hours <= 9:
            self.day_period = 'sunrise/'
        elif self.game_time_hours > 9 and self.game_time_hours <= 19:
            self.day_period = 'day/'
        elif self.game_time_hours > 19 and self.game_time_hours <= 23:
            self.day_period = 'sunset/'
        elif self.game_time_hours >= 0 and self.game_time_hours < 6:
            self.day_period = 'night/'

        return self.day_period


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
            self.spawn_new_sprite(self.cloud_light_sprite,self.path_image + 'cloud-light',CloudLight)

        self.cloud_light_sprite.draw(self.display)
        self.cloud_light_sprite.update()

    def cloud_dark(self):
        if len(self.cloud_dark_sprite) < self.cloud_dark_amount:
            self.spawn_new_sprite(self.cloud_dark_sprite,self.path_image + 'cloud-dark',CloudDark)

        self.cloud_dark_sprite.draw(self.display)
        self.cloud_dark_sprite.update()

    def run(self):
        self.game_time = self.day_time.update()
        self.check_time_period(self.game_time)

        self.display.blit(self.background_image,(0,0))
        self.cloud_dark()
        self.cloud_light()



# General setting of background sprites

class Sprite(pygame.sprite.Sprite):
    def __init__(self, sprite_path, pos_x, pos_y):
        super().__init__()
        self.image = pygame.image.load(sprite_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.topright = [pos_x, pos_y]

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
        self.rect.topright = [self.pos_x,self.pos_y]
        self.pos_x += 1


class CloudDark(Sprite):
    def __init__(self, sprite_path, pos_x, pos_y):
        super().__init__(sprite_path, pos_x, pos_y)

    def update(self):
        self.check_sprite_status()
        self.rect.topright = [self.pos_x,self.pos_y]
        self.pos_x += 0.5






