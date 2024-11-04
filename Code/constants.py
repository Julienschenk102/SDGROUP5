

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

BADDIEMINSPEED = 3
BADDIEMAXSPEED = 5
ADDNEWBADDIERATE = 40
PLAYERMOVERATE = 5
baddieHeight = 0.15 * WINDOWHEIGHT
baddieWidth = int(baddieHeight * 3 / 4)
crowdHeight = baddieHeight
crowdWidth = baddieWidth

# Images.
playerImage = pygame.image.load('player.png')
playerRect = playerImage.get_rect()
baddieImage = pygame.image.load('baddie1.png')
goodImage1 = pygame.image.load('good1.png')
goodImage2 = pygame.image.load('good2.png')
