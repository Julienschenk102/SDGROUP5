

import pygame, random, sys
from pygame.locals import *
pygame.init()

screen_info = pygame.display.Info()
screen_width = screen_info.current_w
screen_height = screen_info.current_h

print(screen_info)
print(screen_width)
print(screen_height)

WINDOWWIDTH = screen_width
WINDOWHEIGHT = screen_height
BORDER = 0.15 * screen_width
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (77, 77, 77)
FPS = 60


PLAYERMOVERATE = 5

#baddie
BADDIEMINSPEED = 3
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 40
baddieHeight = 0.15 * WINDOWHEIGHT
baddieWidth = int(baddieHeight * 3 / 4)

#good
GOODMINSPEED = 3
GOODMAXSPEED = 8
ADDNEWGOODRATE = 2
goodHeight = baddieHeight
goodWidth = baddieWidth

# Images.
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie1.png')
goodImage1 = pygame.image.load('good1.png')
goodImage2 = pygame.image.load('good2.png')

good_image_paths = [
    'good1.png',
    'good2.png',
]
