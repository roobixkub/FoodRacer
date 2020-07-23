# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 08:00:56 2020

@author: Nate
"""

import pygame
# from pygame.locals import (
#         K_UP,
#         K_DOWN,
#         K_LEFT,
#         K_RIGHT,
#         K_ESCAPE,
#         KEYDOWN,
#         QUIT
#     )
from pygame.math import Vector2

# from Config import SCREEN_WIDTH, SCREEN_HEIGHT
from Tools import load_png

class Player(pygame.sprite.Sprite):
    
    def __init__(self, selection, pos, track, *groups):
        super().__init__(*groups)
        self.image, self.rect = load_png(selection)
        self.image = pygame.transform.scale(self.image,(100,100))
        self.rect = self.image.get_rect(center = pos)
        self.mask = pygame.mask.from_surface(self.image)
        self.vel = Vector2(0, 0)
        self.pos = Vector2(pos)
        """ wall collision """
        self.track = track
        self.camera = Vector2(0, 0)
        

    def update(self):
        """ movement independent of display """
        # if pressed_keys[K_UP]:
        #     self.rect.move_ip(0, -5)
        # if pressed_keys[K_DOWN]:
        #     self.rect.move_ip(0, 5)
        # if pressed_keys[K_LEFT]:
        #     self.rect.move_ip(-5, 0)
        # if pressed_keys[K_RIGHT]:
        #     self.rect.move_ip(5, 0)
            
        # if self.rect.left < 0:
        #     self.rect.left = 0
        # if self.rect.right > SCREEN_WIDTH:
        #     self.rect.right = SCREEN_WIDTH
        # if self.rect.top <= 0:
        #     self.rect.top = 0
        # if self.rect.bottom >= SCREEN_HEIGHT:
        #     self.rect.bottom = SCREEN_HEIGHT
        
        """ display centered on player """
        """ change camera position when moving """
        self.camera -= self.vel
        """ horizontal movement, need to convert to rotation """
        self.pos.x += self.vel.x
        self.rect.centerx = self.pos.x
        
        """ change the rect and self.pos coordinates from collision """
        # for track in self.track:
        if not pygame.sprite.spritecollide(self, self.track, False):
            if self.vel.x > 0:
                self.rect.right = self.track.rect.right
            elif self.vel.x < 0:
                self.rect.left = self.track.rect.left
            self.pos.x = self.rect.centerx
            self.camera.x += self.vel.x
        
        """ Vertical movement """
        self.pos.y += self.vel.y
        self.rect.centery = self.pos.y
        
        """ change the rect and self.pos coordinates from colision """
        # for track in self.track: 
        if not pygame.sprite.spritecollide(self, self.track, False):
            if self.vel.y > 0:
                self.rect.bottom = self.track.rect.bottom
            elif self.vel.y < 0:
                self.rect.top = self.track.rect.top
            self.pos.y = self.rect.centery
            self.camera.y += self.vel.y
