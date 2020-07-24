# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:06:31 2020

@author: Nate
"""

import os
import pygame

from Tools import load_png

class Right_turn_up(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(os.path.join('data', 'trackturn.png')).convert()
        self.image = pygame.transform.scale(self.image,(650,650))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.rect = self.image.get_rect(topleft = (x, y))
        
class Left_turn_up(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(os.path.join('data', 'trackturn.png')).convert()
        self.image = pygame.transform.scale(self.image,(650,650))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.image = pygame.transform.rotate(self.image,270)
        self.rect = self.image.get_rect(topleft = (x, y))
        
class Right_turn_down(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(os.path.join('data', 'trackturn.png')).convert()
        self.image = pygame.transform.scale(self.image,(650,650))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.image = pygame.transform.rotate(self.image,180)
        self.rect = self.image.get_rect(topleft = (x, y))
        
class Left_turn_down(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image = pygame.image.load(os.path.join('data', 'trackturn.png')).convert()
        self.image = pygame.transform.scale(self.image,(650,650))
        self.image.set_colorkey(self.image.get_at((0,0)))
        self.image = pygame.transform.rotate(self.image,90)
        self.rect = self.image.get_rect(topleft = (x, y))
        
class Vert_track(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image, self.rect = load_png('track.png')
        self.image = pygame.transform.scale(self.image,(400,650))
        self.rect = self.image.get_rect(topleft = (x, y))
        
class Horiz_track(pygame.sprite.Sprite):
    def __init__(self, x, y, *groups):
        super().__init__(*groups)
        self.image, self.rect = load_png('track.png')
        self.image = pygame.transform.scale(self.image,(400,650))
        self.image = pygame.transform.rotate(self.image,90)
        self.rect = self.image.get_rect(topleft = (x, y))
        

def Build_test():
    test_track = [
            [Right_turn_up, Horiz_track, Horiz_track, Horiz_track, Horiz_track, Horiz_track, Horiz_track, Left_turn_up, None, None], 
            [Vert_track, None, None, None, None, None, None, Vert_track, None, None], 
            [Vert_track, None, Right_turn_up, Horiz_track, Horiz_track, Left_turn_up, None, Vert_track, None, Vert_track], 
            [Vert_track, None, Vert_track, None, None, Vert_track, None, Vert_track, None, Vert_track], 
            [Vert_track, None, Vert_track,None, None, Vert_track, None, Vert_track, None, Vert_track], 
            [Vert_track, None, Vert_track,None, Horiz_track, Right_turn_down, None, Vert_track, None, Vert_track], 
            [Vert_track, None, Vert_track, None, None, None, None, Vert_track, None, Vert_track], 
            [Vert_track, None, Left_turn_down, Horiz_track, Horiz_track, Horiz_track, Horiz_track, Right_turn_down, None, Vert_track], 
            [Vert_track, None, None, None, None, None, None, None, None, Vert_track], 
            [Left_turn_down, Horiz_track, Horiz_track, Horiz_track, Horiz_track, Horiz_track, Horiz_track, Horiz_track, Horiz_track, Right_turn_down]
        ]
    start = (400, 400)
    
    track_group = pygame.sprite.Group()
    y_grid = 0
    x_grid = 0
    for y in range(0, 6500, 650):
        for x in range(0, 6500, 650):
            section = test_track[y_grid][x_grid]
            if section != None:
                track_group.add(section(x, y))
                x_grid += 1
            else:
                x_grid += 1
        y_grid += 1
        x_grid = 0
    return start, track_group
