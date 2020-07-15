# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:12:26 2020

@author: Nate
"""


# imports
import sys
import random
import math
import os
import getopt
import pygame
#from socket import *
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT
)


# global variables
SCREEN_WIDTH = 1600
SCREEN_HEIGHT = 1200
BANANA = 'bananaman.png'

import Racers
import Obstacles

def main():
    # initialize the screen
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Food Racer screen')
    
    # create obstacles add event
    ADDOBSTACLE = pygame.USEREVENT + 1
    pygame.time.set_timer(ADDOBSTACLE, 1000)
    
    # fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    
    # # display some text
    # font = pygame.font.Font(None, 100)
    # text = font.render("Food Racer!!!", 1, (10, 10, 10))
    # textpos = text.get_rect()
    # textpos.centerx = background.get_rect().centerx
    # textpos.centery = background.get_rect().centery
    # background.blit(text, textpos)
    
    # create racers
    player1 = Racers.Player(BANANA)
    
    # create obstacles
    obstacles = pygame.sprite.Group()
    
    # create sprite groups
    all_sprites = pygame.sprite.Group()
    all_sprites.add(player1)
    
    # blit everything to the screen
    pygame.display.flip()
    
    # set game clock
    clock = pygame.time.Clock()
    
    # event loop
    running = True
    while running:     
        # make sure game doesn't run more than 60 fps
        clock.tick(60)
        # event handeler
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    # this will need to be a pause menu instead of exit
                    running = False
            elif event.type == QUIT:
                running = False
            elif event.type == ADDOBSTACLE:
                # create a new obstacle and add it to sprite groups
                new_obstacle = Obstacles.Obstacle()
                obstacles.add(new_obstacle)
                all_sprites.add(new_obstacle)
        # get all the pressed keys
        pressed_keys = pygame.key.get_pressed()
        # update the racers based on key presses
        player1.update(pressed_keys)
        # update obstacles
        obstacles.update()
        # draw screen and update display
        screen.blit(background, (0, 0))
        for entity in all_sprites:
            screen.blit(entity.surf, entity.rect)
            
        for obstacle in obstacles:
            offset = (player1.rect.x - obstacle.rect.x), (player1.rect.y - obstacle.rect.y)
            if obstacle.mask.overlap(player1.mask, offset):
                # poop[0].kill()
                # this will need a game over screen instead
                running = False
        pygame.display.flip()
    pygame.quit()




   


    
if __name__ == '__main__': main()
