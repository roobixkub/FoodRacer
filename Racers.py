# -*- coding: utf-8 -*-
"""
Created on Sat Jul 11 08:00:56 2020

@author: Nate
"""

import pygame
from pygame.math import Vector2

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
        self.camera = Vector2(pos)
        

    def update(self):
        """ display centered on player """
        """ change camera position when moving """
        self.camera -= self.vel
        """ horizontal movement, need to convert to rotation """
        self.pos.x += self.vel.x
        self.rect.centerx = self.pos.x
        
        """ change the rect and self.pos coordinates from collision """
        if not pygame.sprite.spritecollide(self, self.track, False):
            for track in self.track:
                if self.vel.x > 0:
                    self.rect.right = track.rect.right
                elif self.vel.x < 0:
                    self.rect.left = track.rect.left
                self.pos.x = self.rect.centerx
                self.camera.x += self.vel.x
        
        """ Vertical movement """
        self.pos.y += self.vel.y
        self.rect.centery = self.pos.y
        
        """ change the rect and self.pos coordinates from colision """
        if not pygame.sprite.spritecollide(self, self.track, False):
            for track in self.track: 
                if self.vel.y > 0:
                    self.rect.bottom = track.rect.bottom
                elif self.vel.y < 0:
                    self.rect.top = track.rect.top
                self.pos.y = self.rect.centery
                self.camera.y += self.vel.y
