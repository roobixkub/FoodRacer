# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:08:55 2020

@author: Nate
"""


import random
import pygame
import os

from FoodRacer import SCREEN_WIDTH, SCREEN_HEIGHT

def load_png(name):
    """load image and return an image object"""
    fullname = os.path.join('data', name)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
        else:
            image = image.convert_alpha()
    except pygame.error as message:
        print ('Cannot load image:' + fullname)
        raise SystemExit (message)
    return image, image.get_rect()


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstacle, self).__init__()
        self.surf, self.rect = load_png('poop.png')
        self.surf = pygame.transform.scale(self.surf,(60,60))
        self.rect = self.surf.get_rect(
            center=(
                random.randint(int(SCREEN_WIDTH/3), int((SCREEN_WIDTH/3)*2)),
                random.randint(0, 0)
            )
        )
        
        self.mask = pygame.mask.from_surface(self.surf)
        self.speed = 10
        
    def update(self):
        self.rect.move_ip(0, +self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()