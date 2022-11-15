import pygame
import time

from settings import *
from sprites import *


class UI():
    def __init__(self, screen,Class_time):
        self.display = screen

        # Day time
        self.class_time = Class_time

        self.day_time_current = ''
        self.day_time_font = SpriteFont(
            '../graphics/ui/font/FFFFORWARD.TTF',
            (SCREEN_WIDTH / 2, 35),
            32
        )
        # background time
        self.day_time_background = SpriteUI(
            '../graphics/ui/day_time/time_sign.png',
            (SCREEN_WIDTH / 2, 0),
            (8, 6),
            'midtop'
        )

        # Day period

        self.day_period_button = SpriteUI(
            '../graphics/ui/day_period/time_day.png',
            (SCREEN_WIDTH, SCREEN_HEIGHT / 2),
            (4, 4),
            'midright'
        )

        self.day_period_arrow = SpriteUI(
            '../graphics/ui/day_period/time_arrow.png',
            (self.day_period_button.position_x - (self.day_period_button.width / 1.35),
             self.day_period_button.position_y),
            (4,4),
            'center'
        )

        #self.last_time_clickable_period = pygame.time.get_ticks()
        self.cooldown_clickable_period = 0.5
        self.count_clickable_period = 0


        self.day_period_content_active = False
        self.day_period_content = SpriteUI(
            '../graphics/ui/day_period/time_period_background.png',
            (SCREEN_WIDTH,SCREEN_HEIGHT / 2),
            (4,4),
            'midright'
        )

        self.current_day_period = 'day'
        self.day_period_list = []


        self.day_period_sunrise = SpriteUI(
            '../graphics/ui/day_period/sunrise/icon_sunrise.png',
            (SCREEN_WIDTH - (self.day_period_content.width / 1.2),self.day_period_content.position_y),
            (4,4),
            'center'
        )
        self.day_period_list.append(self.day_period_sunrise)

        self.day_period_day = SpriteUI(
            '../graphics/ui/day_period/day/icon_day.png',
            (self.day_period_sunrise.position_x + self.day_period_sunrise.width + 5,self.day_period_content.position_y),
            (4,4),
            'center'
        )
        self.day_period_list.append(self.day_period_day)

        self.day_period_sunset = SpriteUI(
            '../graphics/ui/day_period/sunset/icon_sunset.png',
            (self.day_period_day.position_x + self.day_period_day.width + 5,self.day_period_content.position_y),
            (4, 4),
            'center'
        )
        self.day_period_list.append(self.day_period_sunset)

        self.day_period_night = SpriteUI(
            '../graphics/ui/day_period/night/icon_night.png',
            (self.day_period_sunset.position_x + self.day_period_sunset.width + 5,self.day_period_content.position_y),
            (4,4),
            'center'
        )
        self.day_period_list.append(self.day_period_night)

        # Weather Options

        self.weather_options_background = SpriteUI(
            '../graphics/ui/weather_options/weather_options_background.png',
            (0,SCREEN_HEIGHT),
            (4,4),
            'bottomleft',
            1
        )

        self.weather_list = []

        self.current_weather = 'clear'
        self.weather_icon_width = 100
        self.weather_icon_position_height = SCREEN_HEIGHT - (self.weather_options_background.height / 2)
        self.weather_icon_scale = 4
        self.weather_icon_align = 'center'

        self.weather_options_clear = SpriteUI(
            '../graphics/ui/weather_options/clear/clear.png',
            (100,self.weather_icon_position_height),
            (self.weather_icon_scale,self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_options_clear.spriteLoad('../graphics/ui/weather_options/clear/clear_active.png')
        self.weather_list.append(self.weather_options_clear)


        self.weather_options_cloudiness = SpriteUI(
            '../graphics/ui/weather_options/cloudiness/cloudiness.png',
            (200,self.weather_icon_position_height),
            (self.weather_icon_scale, self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_cloudiness)

        self.weather_options_heavy_cloudiness = SpriteUI(
            '../graphics/ui/weather_options/heavy_cloudiness/heavy_cloudiness.png',
            (300,self.weather_icon_position_height),
            (self.weather_icon_scale,self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_heavy_cloudiness)

        self.weather_options_rainy = SpriteUI(
            '../graphics/ui/weather_options/rainy/rainy.png',
            (400, self.weather_icon_position_height),
            (self.weather_icon_scale, self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_rainy)

        self.weather_options_heavy_rainy = SpriteUI(
            '../graphics/ui/weather_options/heavy_rainy/heavy_rainy.png',
            (500, self.weather_icon_position_height),
            (self.weather_icon_scale, self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_heavy_rainy)

        self.weather_options_snowy = SpriteUI(
            '../graphics/ui/weather_options/snowy/snowy.png',
            (600,self.weather_icon_position_height),
            (self.weather_icon_scale,self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_snowy)

        self.weather_options_heavy_snowy = SpriteUI(
            '../graphics/ui/weather_options/heavy_snowy/heavy_snowy.png',
            (700, self.weather_icon_position_height),
            (self.weather_icon_scale, self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_heavy_snowy)

        self.weather_options_thunder = SpriteUI(
            '../graphics/ui/weather_options/thunder/thunder.png',
            (800, self.weather_icon_position_height),
            (self.weather_icon_scale, self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_thunder)

        self.weather_options_heavy_thunder = SpriteUI(
            '../graphics/ui/weather_options/heavy_thunder/heavy_thunder.png',
            (900, self.weather_icon_position_height),
            (self.weather_icon_scale, self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_heavy_thunder)

        self.weather_options_thunderstorm = SpriteUI(
            '../graphics/ui/weather_options/thunderstorm/thunderstorm.png',
            (1000, self.weather_icon_position_height),
            (self.weather_icon_scale, self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_thunderstorm)

        self.weather_options_heavy_thunderstorm = SpriteUI(
            '../graphics/ui/weather_options/heavy_thunderstorm/heavy_thunderstorm.png',
            (1100, self.weather_icon_position_height),
            (self.weather_icon_scale, self.weather_icon_scale),
            self.weather_icon_align
        )
        self.weather_list.append(self.weather_options_heavy_thunderstorm)


    def day_time(self, day_time_current):
        self.display.blit(self.day_time_background.sprite, self.day_time_background.rect)

        self.day_time_current = day_time_current
        self.day_time_text = self.day_time_font.font.render(self.day_time_current, True, (0, 0, 0))
        self.day_time_text_rect = self.day_time_text.get_rect(
            center=(self.day_time_font.position_x, self.day_time_font.position_y))
        self.display.blit(self.day_time_text, self.day_time_text_rect)

    def day_period(self, mouse_position):
        self.day_time_current_hours = int(self.day_time_current.split(':')[0])

        self.display.blit(self.day_period_button.sprite, self.day_period_button.rect)
        self.display.blit(self.day_period_arrow.sprite, self.day_period_arrow.rect)


        if self.day_period_content_active:
            self.display.blit(self.day_period_content.sprite, self.day_period_content.rect)
            self.display.blit(self.day_period_sunrise.sprite,self.day_period_sunrise.rect)
            self.display.blit(self.day_period_day.sprite,self.day_period_day.rect)
            self.display.blit(self.day_period_sunset.sprite,self.day_period_sunset.rect)
            self.display.blit(self.day_period_night.sprite,self.day_period_night.rect)

            if pygame.mouse.get_pressed()[0]:
                self.current_time_clickable_period = time.time()

                if (self.current_time_clickable_period - self.start_time_clickable_period) >= self.cooldown_clickable_period:
                    if self.day_period_sunrise.rect.collidepoint(mouse_position):
                        self.icon_active(
                            self.day_period_sunrise,
                            '../graphics/ui/day_period/sunrise/icon_sunrise_active.png',
                            'sunrise',
                            self.day_period_list
                        )
                        self.class_time.change_time(6)
                    elif self.day_period_day.rect.collidepoint(mouse_position):
                        self.icon_active(
                            self.day_period_day,
                            '../graphics/ui/day_period/day/icon_day_active.png',
                            'day',
                            self.day_period_list
                        )
                        self.class_time.change_time(9)
                    elif self.day_period_sunset.rect.collidepoint(mouse_position):
                        self.icon_active(
                            self.day_period_sunset,
                            '../graphics/ui/day_period/sunset/icon_sunset_active.png',
                            'sunset',
                            self.day_period_list
                        )
                        self.class_time.change_time(19)
                    elif self.day_period_night.rect.collidepoint(mouse_position):
                        self.icon_active(
                            self.day_period_night,
                            '../graphics/ui/day_period/night/icon_night_active.png',
                            'night',
                            self.day_period_list
                        )
                        self.class_time.change_time(0)

        if pygame.mouse.get_pressed()[0] and self.day_period_button.rect.collidepoint(mouse_position):
            self.day_period_button.slide(1,SCREEN_WIDTH - self.day_period_content.width,False)
            self.day_period_arrow.slide(1, SCREEN_WIDTH - self.day_period_content.width - (self.day_period_button.width/1.35),True)
            if self.day_period_content_active:
                self.day_period_content_active = False
            elif not(self.day_period_content_active):
                self.day_period_content_active = True
                self.start_time_clickable_period = time.time()

    def set_active_period(self):
        if self.class_time.game_hour >= 6 and self.class_time.game_hour < 9:
            self.icon_active(
                self.day_period_sunrise,
                '../graphics/ui/day_period/sunrise/icon_sunrise_active.png',
                'sunrise',
                self.day_period_list
            )
        elif self.class_time.game_hour >= 9 and self.class_time.game_hour < 19:
            self.icon_active(
                self.day_period_day,
                '../graphics/ui/day_period/day/icon_day_active.png',
                'day',
                self.day_period_list
            )
        elif self.class_time.game_hour >= 19 and self.class_time.game_hour < 23:
            self.icon_active(
                self.day_period_sunset,
                '../graphics/ui/day_period/sunset/icon_sunset_active.png',
                'sunset',
                self.day_period_list
            )
        elif self.class_time.game_hour >= 0 and self.class_time.game_hour < 6:
            self.icon_active(
                self.day_period_night,
                '../graphics/ui/day_period/night/icon_night_active.png',
                'night',
                self.day_period_list
            )

    def weather_options(self,mouse_position):
        self.display.blit(self.weather_options_background.sprite, self.weather_options_background.rect)

        self.weather_blit()

        if pygame.mouse.get_pressed()[0]:
            if self.weather_options_clear.rect.collidepoint(mouse_position):
                self.icon_active(
                    self.weather_options_clear,
                    '../graphics/ui/weather_options/clear/clear_active.png',
                    'clear',
                    self.weather_list
                )
                self.current_weather = 'clear'
            elif self.weather_options_cloudiness.rect.collidepoint(mouse_position):
                self.icon_active(
                    self.weather_options_cloudiness,
                    '../graphics/ui/weather_options/cloudiness/cloudiness_active.png',
                    'cloudiness',
                    self.weather_list
                )
                self.current_weather = 'cloudiness'
            elif self.weather_options_heavy_cloudiness.rect.collidepoint(mouse_position):
                self.icon_active(
                    self.weather_options_heavy_cloudiness,
                    '../graphics/ui/weather_options/heavy_cloudiness/heavy_cloudiness_active.png',
                    'heavy_cloudiness',
                    self.weather_list
                )
                self.current_weather = 'heavy_cloudiness'
            elif self.weather_options_rainy.rect.collidepoint(mouse_position) and self.current_weather != 'rainy':
                self.icon_active(
                    self.weather_options_rainy,
                    '../graphics/ui/weather_options/rainy/rainy_active.png',
                    'rainy',
                    self.weather_list
                )
                self.current_weather = 'rainy'
            elif self.weather_options_heavy_rainy.rect.collidepoint(mouse_position) and self.current_weather != 'heavy_rainy':
                self.icon_active(
                    self.weather_options_heavy_rainy,
                    '../graphics/ui/weather_options/heavy_rainy/heavy_rainy_active.png',
                    'heavy_rainy',
                    self.weather_list
                )
                self.current_weather = 'heavy_rainy'
            elif self.weather_options_snowy.rect.collidepoint(mouse_position) and self.current_weather != 'snowy':
                self.icon_active(
                    self.weather_options_snowy,
                    '../graphics/ui/weather_options/snowy/snowy_active.png',
                    'snowy',
                    self.weather_list
                )
                self.current_weather = 'snowy'
            elif self.weather_options_heavy_snowy.rect.collidepoint(mouse_position) and self.current_weather != 'heavy_snowy':
                self.icon_active(
                    self.weather_options_heavy_snowy,
                    '../graphics/ui/weather_options/heavy_snowy/heavy_snowy_active.png',
                    'heavy_snowy',
                    self.weather_list
                )
                self.current_weather = 'heavy_snowy'
            elif self.weather_options_thunder.rect.collidepoint(mouse_position) and self.current_weather != 'thunder':
                self.icon_active(
                    self.weather_options_thunder,
                    '../graphics/ui/weather_options/thunder/thunder_active.png',
                    'thunder',
                    self.weather_list
                )
                self.current_weather = 'thunder'
            elif self.weather_options_heavy_thunder.rect.collidepoint(mouse_position) and self.current_weather != 'heavy_thunder':
                self.icon_active(
                    self.weather_options_heavy_thunder,
                    '../graphics/ui/weather_options/heavy_thunder/heavy_thunder_active.png',
                    'heavy_thunder',
                    self.weather_list
                )
                self.current_weather = 'heavy_thunder'
            elif self.weather_options_thunderstorm.rect.collidepoint(mouse_position) and self.current_weather != 'thunderstorm':
                self.icon_active(
                    self.weather_options_thunderstorm,
                    '../graphics/ui/weather_options/thunderstorm/thunderstorm_active.png',
                    'thunderstorm',
                    self.weather_list
                )
                self.current_weather = 'thunderstorm'
            elif self.weather_options_heavy_thunderstorm.rect.collidepoint(mouse_position) and self.current_weather != 'heavy_thunderstorm':
                self.icon_active(
                    self.weather_options_heavy_thunderstorm,
                    '../graphics/ui/weather_options/heavy_thunderstorm/heavy_thunderstorm_active.png',
                    'heavy_thunderstorm',
                    self.weather_list
                )
                self.current_weather = 'heavy_thunderstorm'

    def weather_blit(self):
        for weather in self.weather_list:
            self.display.blit(weather.sprite, weather.rect)

    def sprite_reset(self, spite_avoid,reset_list):
        for sprite_object in reset_list:
            if sprite_object.sprite == spite_avoid:
                continue
            sprite_object.resetSprite()

    def icon_active(self, icon_class, icon_path_active, icon_name,icon_list):
        icon_class.spriteLoad(icon_path_active)
        self.sprite_reset(icon_class.sprite,icon_list)


    def run(self, time):
        self.set_active_period()
        self.day_time(time)
        self.day_period(pygame.mouse.get_pos())
        self.weather_options(pygame.mouse.get_pos())


