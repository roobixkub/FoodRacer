# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:06:31 2020

@author: Nate
"""

import random
import pygame

from Tools import load_png

class Right_turn_up(pygame.sprite.Sprite):
    def __init__(self):
        super(Right_turn_up, self).__init__()
        self.surf, self.rect = load_png('trackturn.png')
        self.surf = pygame.transform.scale(self.surf,(650,650))
        
class Left_turn_up(pygame.sprite.Sprite):
    def __init__(self):
        super(Right_turn_up, self).__init__()
        self.surf, self.rect = load_png('trackturn.png')
        self.surf = pygame.transform.scale(self.surf,(650,650))
        self.surf = pygame.transform.rotate(self.surf,270)
        
class Right_turn_down(pygame.sprite.Sprite):
    def __init__(self):
        super(Right_turn_down, self).__init__()
        self.surf, self.rect = load_png('trackturn.png')
        self.surf = pygame.transform.scale(self.surf,(650,650))
        self.surf = pygame.transform.rotate(self.surf,180)
        
class Left_turn_down(pygame.sprite.Sprite):
    def __init__(self):
        super(Left_turn_down, self).__init__()
        self.surf, self.rect = load_png('trackturn.png')
        self.surf = pygame.transform.scale(self.surf,(650,650))
        self.surf = pygame.transform.rotate(self.surf,90)
        
class Vert_track(pygame.sprite.Sprite):
    def __init__(self):
        super(Vert_track, self).__init__()
        self.surf, self.rect = load_png('track.png')
        self.surf = pygame.transform.scale(self.surf,(650,650))
        
class Horiz_track(pygame.sprite.Sprite):
    def __init__(self):
        super(Horiz_track, self).__init__()
        self.surf, self.rect = load_png('track.png')
        self.surf = pygame.transform.scale(self.surf,(650,650))
        self.surf = pygame.transform.rotate(self.surf,90)
        
        