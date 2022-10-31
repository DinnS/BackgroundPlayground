import pygame
from settings import *

class Day_menu():
    def __init__(self,screen):
        self.display = screen

        self.menu_width = SCREEN_WIDTH
        self.menu_height = (SCREEN_HEIGHT / 6)

        self.position_x = 0
        self.position_y = SCREEN_HEIGHT - self.menu_height

        self.menu_image = pygame.image.load('../graphics/day_menu/day_menu.png')
        print(self.menu_image.get_height())
        #self.menu_image = pygame.transform.scale(self.menu_image,(self.menu_width,self.menu_height))
        self.menu_image_rect = self.menu_image.get_rect(bottomright = (0,0))
        print(self.menu_image.get_height())

        # Text
        self.menu_font = pygame.font.Font('../graphics/font/FFFFORWARD.TTF',32)
        self.menu_text = self.menu_font.render('12:30',True,(0,0,0))
        self.menu_text_rect = self.menu_text.get_rect(center = (self.menu_width - 400,950))

    def run(self):

        self.display.blit(self.menu_image,(0,0))
        #self.display.blit(self.menu_text, self.menu_text_rect)