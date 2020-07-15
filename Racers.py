# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 08:00:56 2020

@author: Nate
"""

import pygame
import os
from pygame.locals import (
        K_UP,
        K_DOWN,
        K_LEFT,
        K_RIGHT,
        K_ESCAPE,
        KEYDOWN,
        QUIT
    )

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


class Player(pygame.sprite.Sprite):
    def __init__(self, selection):
        super(Player, self).__init__()
        self.surf, self.rect = load_png(selection)
        self.surf = pygame.transform.scale(self.surf,(100,100))
        self.rect = self.surf.get_rect(
            center = (SCREEN_WIDTH/2, SCREEN_HEIGHT - 100)
        )
        self.mask = pygame.mask.from_surface(self.surf)

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
            
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

