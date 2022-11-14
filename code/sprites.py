import pygame
from settings import *

class SpriteUI:
    def __init__(self,image_path,position,scale,align,full_screen = 0):
        self.sprite = pygame.image.load(image_path).convert_alpha()
        self.beginner_sprite = self.sprite
        if full_screen == 1:
            self.width = SCREEN_WIDTH
        else:
            self.width = self.sprite.get_width() * scale[0]

        self.height = self.sprite.get_height() * scale[1]
        self.position_x = position[0]
        self.position_y = position[1]
        self.align = align
        self.sprite = pygame.transform.scale(self.sprite,(self.width,self.height))

        self.start_position_x = self.position_x
        self.start_position_y = self.position_y

        self.assignRect()

    def spriteLoad(self,sprite_path):
        self.sprite = pygame.image.load(sprite_path).convert_alpha()
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))

    def resetSprite(self):
        self.sprite = self.beginner_sprite
        self.sprite = pygame.transform.scale(self.sprite, (self.width, self.height))


    def slide(self,speed,end_point,rotate):
        if self.rect.midleft[0] > end_point:
            self.position_x = end_point
            if rotate:
                self.sprite = pygame.transform.rotate(self.sprite,180)
        elif self.rect.midleft[0] < end_point:
            self.position_x = self.start_position_x
            if rotate:
                self.sprite = pygame.transform.rotate(self.sprite,180)

        self.assignRect()


    def assignRect(self):
        if self.align == 'midtop':
            self.rect = self.sprite.get_rect(midtop=(self.position_x, self.position_y))
        elif self.align == 'midright':
            self.rect = self.sprite.get_rect(midright=(self.position_x, self.position_y))
        elif self.align == 'center':
            self.rect = self.sprite.get_rect(center=(self.position_x, self.position_y))
        elif self.align == 'topleft':
            self.rect = self.sprite.get_rect(topleft=(self.position_x, self.position_y))
        elif self.align == 'bottomleft':
            self.rect = self.sprite.get_rect(bottomleft =(self.position_x, self.position_y))



class SpriteFont:
    def __init__(self,font_path,position,font_size):
        self.font = pygame.font.Font(font_path,font_size)
        self.position_x = position[0]
        self.position_y = position[1]
