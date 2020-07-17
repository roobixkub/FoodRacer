# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:06:31 2020

@author: Nate
"""

import os
import random
import pygame

from Tools import load_png

class Right_turn_up(pygame.sprite.Sprite):
    def __init__(self):
        super(Right_turn_up, self).__init__()
        self.surf = pygame.image.load(os.path.join('data', 'trackturn.png')).convert()
        self.surf = pygame.transform.scale(self.surf,(650,650))
        self.surf.set_colorkey(self.surf.get_at((0,0)))

class Left_turn_up(pygame.sprite.Sprite):
    def __init__(self):
        super(Left_turn_up, self).__init__()
        self.surf = pygame.image.load(os.path.join('data', 'trackturn.png')).convert()
        self.surf = pygame.transform.scale(self.surf,(650,650))
        self.surf.set_colorkey(self.surf.get_at((0,0)))
        self.surf = pygame.transform.rotate(self.surf,270)

class Right_turn_down(pygame.sprite.Sprite):
    def __init__(self):
        super(Right_turn_down, self).__init__()
        self.surf = pygame.image.load(os.path.join('data', 'trackturn.png')).convert()
        self.surf = pygame.transform.scale(self.surf,(650,650))
        self.surf.set_colorkey(self.surf.get_at((0,0)))
        self.surf = pygame.transform.rotate(self.surf,180)

class Left_turn_down(pygame.sprite.Sprite):
    def __init__(self):
        super(Left_turn_down, self).__init__()
        self.surf = pygame.image.load(os.path.join('data', 'trackturn.png')).convert()
        self.surf = pygame.transform.scale(self.surf,(650,650))
        self.surf.set_colorkey(self.surf.get_at((0,0)))
        self.surf = pygame.transform.rotate(self.surf,90)

class Vert_track(pygame.sprite.Sprite):
    def __init__(self):
        super(Vert_track, self).__init__()
        self.surf, self.rect = load_png('track.png')
        self.surf = pygame.transform.scale(self.surf,(400,650))
        

class Horiz_track(pygame.sprite.Sprite):
    def __init__(self):
        super(Horiz_track, self).__init__()
        self.surf, self.rect = load_png('track.png')
        self.surf = pygame.transform.scale(self.surf,(400,650))
        self.surf = pygame.transform.rotate(self.surf,90)


def Build_test():
    test_track = [
            [Right_turn_up().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Left_turn_up().surf, None, None], 
            [Vert_track().surf, None, None, None, None, None, None, Vert_track().surf, None, None], 
            [Vert_track().surf, None, Right_turn_up().surf, Horiz_track().surf, Horiz_track().surf, Left_turn_up().surf, None, Vert_track().surf, None, Vert_track().surf], 
            [Vert_track().surf, None, Vert_track().surf, None, None, Vert_track().surf, None, Vert_track().surf, None, Vert_track().surf], 
            [Vert_track().surf, None, Vert_track().surf,None, None, Vert_track().surf, None, Vert_track().surf, None, Vert_track().surf], 
            [Vert_track().surf, None, Vert_track().surf,None, Horiz_track().surf, Right_turn_down().surf, None, Vert_track().surf, None, Vert_track().surf], 
            [Vert_track().surf, None, Vert_track().surf, None, None, None, None, Vert_track().surf, None, Vert_track().surf], 
            [Vert_track().surf, None, Left_turn_down().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Right_turn_down().surf, None, Vert_track().surf], 
            [Vert_track().surf, None, None, None, None, None, None, None, None, Vert_track().surf], 
            [Left_turn_down().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Horiz_track().surf, Right_turn_down().surf], 
        ]
    return test_track

    
