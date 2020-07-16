# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 23:45:11 2020

@author: Nate
"""

import os
import pygame

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

