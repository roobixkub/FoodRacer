# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 09:08:55 2020

@author: Nate
"""


import random
import pygame

from Config import SCREEN_WIDTH, SCREEN_HEIGHT
from Tools import load_png

class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstacle, self).__init__()
        self.surf, self.rect = load_png('gumdrop.png')
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