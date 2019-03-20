import pygame, sys
from pygame.locals import *

#Setup Pygame
pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 800))
pygame.display.set_caption("Shao Lin's Road")
fpsClock = pygame.time.Clock()
FPS = 60

# --- Assest Loading

#Hero Img
heroImg = pygame.image.load('Assets/hero.png')
heroImg = pygame.transform.scale(heroImg, (200, 200))
#Hero kick right
herokickImg = pygame.image.load('Assets/herokick.png')
herokickImg = pygame.transform.scale(herokickImg, (200, 200))

#hero kick left
herokickImg2 = pygame.image.load('Assets/herokick.png')
herokickImg2 = pygame.transform.scale(herokickImg2, (200, 200))
herokickImg2 = pygame.transform.flip(herokickImg2, True, False)

#Enemy Img
enemyImg = pygame.image.load('Assets/enemy.png')
enemyImg = pygame.transform.scale(enemyImg, (200, 200))

class Enemy():
    def __init__(self):
        self.x = enemyX
        self.y = enemyY

    def blit(self):
        self.blit = DISPLAYSURF.blit(enemyImg, (enemyX, enemyY))

#Background Img
bg = pygame.image.load("Assets/background.png")
bg = pygame.transform.scale(bg, (800, 800))

#variables
heroX = 650
heroY = 550 
enemyX = 400
enemyY = 253



kicking = False
while True: # main game loop

    #Draw background
    DISPLAYSURF.blit(bg, (0, 0))

    #Enemy logic 
    if enemyX < 750 :
        enemyX = enemyX - 1

    if enemyX > 200:
        enemyX = enemyX + 2
            
    enemy = Enemy()
    enemy.blit()
 
    #Hero Logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and heroX > -50: 
        heroX -= 10

    if keys[pygame.K_RIGHT] and heroX < 650:
        heroX += 10
        
    if keys[pygame.K_SPACE] and keys[pygame.K_RIGHT]:
        kicking = True
        DISPLAYSURF.blit(herokickImg, (heroX, heroY))

    if keys[pygame.K_SPACE] and keys[pygame.K_LEFT]:
        kicking = True
        DISPLAYSURF.blit(herokickImg2, (heroX, heroY))
        
    else:
        kicking = False
        DISPLAYSURF.blit(heroImg, (heroX, heroY))


    fpsClock.tick(FPS)
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()



    
