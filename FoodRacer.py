# -*- coding: utf-8 -*-
"""
Created on Fri Jul 10 13:12:26 2020

@author: Nate
"""


""" general imports """
import os
import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    KEYUP,
    QUIT
)


""" global variables """
RACERS = {'BANANA': 'bananaman.png'}
BACKGROUNDS = {'CANDY': 'candymap.png'}

""" unique imports """
from Config import SCREEN_WIDTH, SCREEN_HEIGHT
import Racers
#import Obstacles
import Track


class Background(pygame.sprite.Sprite):
    def __init__(self, surface, location):
        pygame.sprite.Sprite.__init__(self)
        self.surf = surface
        self.rect = self.surf.get_rect(topleft=location)
        
""" main game function """
def main():
    """ initialize the screen """
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Food Racer')
    
    """ create obstacles add event """
    # ADDOBSTACLE = pygame.USEREVENT + 1
    # pygame.time.set_timer(ADDOBSTACLE, 1000)
    
    """ set background """
    background = pygame.Surface((13000, 13000))
    background_tile = pygame.image.load(os.path.join('data', BACKGROUNDS['CANDY']))
    background_tile = background_tile.convert()
    
    for y in range(0, 13000, 1300):
        for x in range(0, 13000, 1300):
            background.blit(background_tile, (x, y))
    
    background = Background(background, [0, 0])        

    """ create obstacles """
    # obstacles = pygame.sprite.Group()

    """ create sprite groups """
    all_sprites = pygame.sprite.Group()
    for track in Track.Build_test()[1]:
        all_sprites.add(track)
    
    """ create racers """
    player1 = Racers.Player(RACERS['BANANA'], (SCREEN_WIDTH/2, SCREEN_HEIGHT/2), Track.Build_test()[1], all_sprites)
    
    """ set game clock """
    clock = pygame.time.Clock()

    """ gameplay loop """
    running = True
    while running:     
        """ make sure game doesn't run more than 60 fps """
        clock.tick(60)
        """ event handeler """
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    """ this will need to be a pause menu instead of exit """
                    running = False
                elif event.key == pygame.K_RIGHT:
                    player1.vel.x = 20
                elif event.key == pygame.K_LEFT:
                    player1.vel.x = -20
                elif event.key == pygame.K_UP:
                    player1.vel.y = -20
                elif event.key == pygame.K_DOWN:
                    player1.vel.y = 20
            elif event.type == KEYUP:
                if event.key == pygame.K_RIGHT and player1.vel.x > 0:
                    player1.vel.x = 0
                elif event.key == pygame.K_LEFT and player1.vel.x < 0:
                    player1.vel.x = 0
                elif event.key == pygame.K_UP and player1.vel.y < 0:
                    player1.vel.y = 0
                elif event.key == pygame.K_DOWN and player1.vel.y > 0:
                    player1.vel.y = 0
            elif event.type == QUIT:
                running = False
            """ add random obstacles via timed event """
            # elif event.type == ADDOBSTACLE:
            #     """ create a new obstacle and add it to sprite groups """
            #     new_obstacle = Obstacles.Obstacle()
            #     obstacles.add(new_obstacle)
            #     all_sprites.add(new_obstacle)
        """ get all the pressed keys """
        # pressed_keys = pygame.key.get_pressed()
        """ update the racers based on key presses """
        # player1.update(pressed_keys)
        """ update obstacles """
        # obstacles.update()
        all_sprites.update()
        """ draw screen and update display """
        screen.blit(background.surf, background.rect)
        for sprite in all_sprites:
            screen.blit(sprite.image, sprite.rect.topleft+player1.camera)
        """ collision detection and handling """   
        # for obstacle in obstacles:
        #     offset = (player1.rect.x - obstacle.rect.x), (player1.rect.y - obstacle.rect.y)
        #     if obstacle.mask.overlap(player1.mask, offset):
        #       """ this will need a game over screen instead """
        #       running = False
        pygame.display.flip()
    




   


    
if __name__ == '__main__': 
    pygame.init()
    main()
    pygame.quit()