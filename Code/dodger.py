import pygame, random, sys
from pygame.locals import *
import constants as cs

#Termine proprement le jeu en fermant Pygame et en quittant le programme
def terminate():
    pygame.quit()
    sys.exit()

#Attend que le joueur appuie sur une touche pour continuer. Si le joueur appuie sur ESC, le programme se termine.
def waitForPlayerToPressKey():
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE: # Pressing ESC quits.
                    terminate()
                return
#Vérifie si le joueur entre en collision avec l'un des ennemis (baddies). Retourne True si une collision est détectée.
def playerHasHitBaddie(playerRect, baddies):
    for b in baddies:
        if playerRect.colliderect(b['rect']):
            return True
    return False

#Dessine du texte à un emplacement donné sur une surface avec une police spécifique.
def drawText(text, font, surface, x, y):
    textobj = font.render(text, 1, cs.TEXTCOLOR)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)

# Initialise Pygame, crée une fenêtre de jeu avec une taille définie dans le fichier constants.py et cache le curseur de la souris.
pygame.init()
mainClock = pygame.time.Clock()
windowSurface = pygame.display.set_mode((cs.WINDOWWIDTH, cs.WINDOWHEIGHT))
pygame.display.set_caption('Dodger')
pygame.mouse.set_visible(False)

# Définit une police avec une taille de 48 pixels.
font = pygame.font.SysFont(None, 48)

#Charge un son pour l’écran de "Game Over".
gameOverSound = pygame.mixer.Sound('gameover.wav')


# Set up images.
playerImage = cs.playerImage
playerRect = playerImage.get_rect()


# Remplit la fenêtre avec une couleur de fond, affiche le titre du jeu et attend que le joueur appuie sur une touche pour commencer.
windowSurface.fill(cs.BACKGROUNDCOLOR)
drawText('Dodger', font, windowSurface, (cs.WINDOWWIDTH / 3), (cs.WINDOWHEIGHT / 3))
drawText('Press a key to start.', font, windowSurface, (cs.WINDOWWIDTH / 3) - 30, (cs.WINDOWHEIGHT / 3) + 50)
pygame.display.update()
waitForPlayerToPressKey()



topScore = 0
while True:
    # Set up the start of the game.
    pygame.mixer.music.load('HypeSound.wav')
    baddies = []
    good = []
    score = 0
    playerRect.topleft = (cs.WINDOWWIDTH / 2, cs.WINDOWHEIGHT - 50)
    moveLeft = moveRight = moveUp = moveDown = False
    reverseCheat = slowCheat = False
    baddieAddCounter = 0
    pygame.mixer.music.play(-1, 0.0)

    while True: # The game loop runs while the game part is playing.
        score += 1 # Increase score.

        for event in pygame.event.get():
            if event.type == QUIT:
                terminate()

            if event.type == KEYDOWN:
                if event.key == K_z:
                    reverseCheat = True
                if event.key == K_x:
                    slowCheat = True
                if event.key == K_LEFT or event.key == K_a:
                    moveRight = False
                    moveLeft = True
                if event.key == K_RIGHT or event.key == K_d:
                    moveLeft = False
                    moveRight = True
                if event.key == K_UP or event.key == K_w:
                    moveDown = False
                    moveUp = True
                if event.key == K_DOWN or event.key == K_s:
                    moveUp = False
                    moveDown = True

            if event.type == KEYUP:
                if event.key == K_z:
                    reverseCheat = False
                    score = 0
                if event.key == K_x:
                    slowCheat = False
                    score = 0
                if event.key == K_ESCAPE:
                        terminate()

                if event.key == K_LEFT or event.key == K_a:
                    moveLeft = False
                if event.key == K_RIGHT or event.key == K_d:
                    moveRight = False
                if event.key == K_UP or event.key == K_w:
                    moveUp = False
                if event.key == K_DOWN or event.key == K_s:
                    moveDown = False

            if event.type == MOUSEMOTION:
                # If the mouse moves, move the player where to the cursor.
                playerRect.centerx = event.pos[0]
                playerRect.centery = event.pos[1]
        # Add new baddies at the top of the screen, if needed.
        if not reverseCheat and not slowCheat:
            baddieAddCounter += 1
        if baddieAddCounter == cs.ADDNEWBADDIERATE:
            baddieAddCounter = 0
            newBaddie = {
    'rect': pygame.Rect(
        random.randint(
            int(cs.BORDER), 
            int(cs.WINDOWWIDTH - cs.baddieWidth - cs.BORDER)
        ), 
        -cs.baddieHeight,  # Commencer au-dessus de l'écran
        cs.baddieWidth, 
        cs.baddieHeight
    ),
    'speed': random.randint(cs.BADDIEMINSPEED, cs.BADDIEMAXSPEED),
    'surface': pygame.transform.scale(cs.baddieImage, (cs.baddieWidth, cs.baddieHeight)),
}

            baddies.append(newBaddie)

        # Move the player around.
        if moveLeft and playerRect.left > 0:
            playerRect.move_ip(-1 * cs.PLAYERMOVERATE, 0)
        if moveRight and playerRect.right < cs.WINDOWWIDTH:
            playerRect.move_ip(cs.PLAYERMOVERATE, 0)
        if moveUp and playerRect.top > 0:
            playerRect.move_ip(0, -1 * cs.PLAYERMOVERATE)
        if moveDown and playerRect.bottom < cs.WINDOWHEIGHT:
            playerRect.move_ip(0, cs.PLAYERMOVERATE)

        # Move the baddies down.
        for b in baddies:
            if not reverseCheat and not slowCheat:
                b['rect'].move_ip(0, b['speed'])
            elif reverseCheat:
                b['rect'].move_ip(0, -5)
            elif slowCheat:
                b['rect'].move_ip(0, 1)

        # Delete baddies that have fallen past the bottom.
        for b in baddies[:]:
            if b['rect'].top > cs.WINDOWHEIGHT:
                baddies.remove(b)

        # Draw the game world on the window.
        windowSurface.fill(cs.BACKGROUNDCOLOR)

        # Draw the score and top score.
        drawText('Score: %s' % (score), font, windowSurface, 10, 0)
        drawText('Top Score: %s' % (topScore), font, windowSurface, 10, 40)

        # Draw the player's rectangle.
        windowSurface.blit(playerImage, playerRect)

        # Draw each baddie.
        for b in baddies:
            windowSurface.blit(b['surface'], b['rect'])

        pygame.display.update()

        # Check if any of the baddies have hit the player.
        if playerHasHitBaddie(playerRect, baddies):
            if score > topScore:
                topScore = score # set new top score
            break

        mainClock.tick(cs.FPS)

    # Stop the game and show the "Game Over" screen.
    pygame.mixer.music.stop()
    gameOverSound.play()

    drawText('GAME OVER', font, windowSurface, cs.WINDOWWIDTH // 2, cs.WINDOWHEIGHT // 3)

    drawText('Press a key to play again.', font, windowSurface, (cs.WINDOWWIDTH / 2) - 80, (cs.WINDOWHEIGHT / 2) + 50)
    pygame.display.update()
    waitForPlayerToPressKey()

    gameOverSound.stop()
