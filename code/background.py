import pygame

from settings import *
from support import import_name_sprite

class Background:
    def __init__(self,screen,current_day_time,Class_ui):
        self.display = screen

        self.ui = Class_ui

        # Setup day time and start day period
        self.game_time = current_day_time

        self.background_animation_index = 0
        self.background_animation_speed = 0.05

        self.current_weather = self.ui.current_weather
        self.day_period = self.check_time_period(self.game_time)
        self.path_image = '../graphics/background/' + self.day_period


        # Weather setup


        # Background
        self.update_background()

    def update_background(self):
        self.path_image = '../graphics/background/' + self.day_period
        self.background_image_list = import_name_sprite(self.path_image + self.current_weather)

        if self.background_animation_index >= len(self.background_image_list):
            self.background_animation_index = 0

        self.background_image = pygame.image.load(self.background_image_list[int(self.background_animation_index)])
        self.background_image = pygame.transform.scale(self.background_image, (SCREEN_WIDTH, SCREEN_HEIGHT))

        self.background_animation_index += self.background_animation_speed

    def check_time_period(self,game_time):
        self.game_time_hours = int(game_time.split(':')[0])

        if self.game_time_hours >= 6 and self.game_time_hours < 9:
            self.day_period = 'sunrise/'
        elif self.game_time_hours >= 9 and self.game_time_hours < 19:
            self.day_period = 'day/'
        elif self.game_time_hours >= 19 and self.game_time_hours < 23:
            self.day_period = 'sunset/'
        elif self.game_time_hours >= 0 and self.game_time_hours < 6:
            self.day_period = 'night/'


        return self.day_period


    def setup_weather(self):
        self.current_weather = self.ui.current_weather
        # if current_weather == 'clear':
        #     self.current_weather = 'clear'
        #     print('clear')
        # elif current_weather == 'cloudiness':
        #     self.current_weather = 'cloudiness'
        #     print('cloudiness')
        # elif current_weather == 'heavy_cloudiness':
        #     self.current_weather = 'heavy_cloudiness'
        #     print('heavy_cloudiness')
        # elif current_weather == 'rainy':
        #     self.current_weather = 'rainy'
        #     print('rainy')
        # elif current_weather == 'heavy_rainy':
        #     self.current_weather = 'heavy_rainy'
        #     print('heavy_rainy')
        # elif current_weather == 'snowy':
        #     self.current_weather = 'snowy'
        #     print('snowy')
        # elif current_weather == 'heavy_snowy':
        #     self.current_weather = 'heavy_snowy'
        #     print('heavy_snowy')
        # elif current_weather == 'thunder':
        #     self.current_weather = 'thunder'
        #     print('thunder')
        # elif current_weather == 'heavy_thunder':
        #     self.current_weather = 'heavy_thunder'
        #     print('heavy_thunder')
        # elif current_weather == 'thunderstorm':
        #     self.current_weather = 'thunderstorm'
        #     print('thunderstorm')
        # elif current_weather == 'heavy_thunderstorm':
        #     self.current_weather = 'heavy_thunderstorm'
        #     print('heavy_thunderstorm')


    def run(self,current_day_time):
        self.game_time = current_day_time
        self.check_time_period(self.game_time)
        self.update_background()
        self.setup_weather()

        self.display.blit(self.background_image,(0,0))


