
#imports
import pygame
from pygame.locals import *
import time
import math
import random
import requests
import io
import urllib.request import urlopen #terminal says it's an error

pygame.init()

# create the game
game_width = 500
game_height = 500
size = (game_width, game_height)
game = pygame.display.set_mode(size)
pygame.display.set_caption('Pokemon Battle')


# define colors

black = (0, 0, 0)
gold = (218, 165, 32)
grey = (0, 200, 200)
green = (0, 200, 0)
red = (200, 0, 0)
white = (255, 255, 255)

#base url of  API
base_url = 'https://pokeapi.co/api/v2'


#class
class Pokemon(pygame):
    def __init__(self, name, height, weight):
        self.name = name
        self.weight = weight
        self.height = height

#characters
pikachu = Pokemon ()
https://pokeapi.co/api/v2/pokemon/pikachu
self.name = name
self.weight = weight
self.height = height

aegislash = Pokemon ()
https://pokeapi.co/api/v2/pokemon-species/aegislash
self.name = name
self.weight = weight
self.height = height


ditto = Pokemon ()
https://pokeapi.co/api/v2/pokemon/ditto
self.name = name
self.weight = weight
self.height = height




#game loop

game_status = 'select pokemon'
while game_status = 'quit':
    
    for event in pygame.event.get():
        if event.type == QUIT:
            game_status = 'quit'

    if game_status == 'select pokemon':

    elif game_status == 'battle':


pygame.quit()



#i know i did this wrong. I will have to resubmit. Didn't have enough time today to brainstrom.
