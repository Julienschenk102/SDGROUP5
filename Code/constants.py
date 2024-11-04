

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
print(BORDER)
TEXTCOLOR = (0, 0, 0)
BACKGROUNDCOLOR = (250, 0, 0)
FPS = 60


PLAYERMOVERATE = 5

#baddie
BADDIEMINSPEED = 3
BADDIEMAXSPEED = 8
ADDNEWBADDIERATE = 40
baddieHeight = 0.15 * WINDOWHEIGHT
baddieWidth = int(baddieHeight * 3 / 4)

#good
GOODMINSPEED = BADDIEMINSPEED
GOODMAXSPEED = BADDIEMAXSPEED
ADDNEWGOODRATE = 2
goodHeight = baddieHeight
goodWidth = baddieWidth

# Images.
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie1.png')

good_image_paths = [
    'PhotosGood/good1.png',
    'PhotosGood/good2.png',
    'PhotosGood/good3.png',
    'PhotosGood/good4.png',
    'PhotosGood/good5.png',
    'PhotosGood/good6.png',
    'PhotosGood/good7.png',
    'PhotosGood/good8.png',
]
