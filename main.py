import pygame
import sys
from Level import Level

pygame.init()
WIDTH = 1280
HEIGHT = 720
screen = pygame.display.set_mode([WIDTH, HEIGHT])
screen.fill((0, 0, 0))


def drawLevel(matrix_to_draw):
    # Load images
    background = pygame.image.load('assets/backgrounds/background.jpg')
    player = pygame.image.load('assets/objects/player.png')

    # Resize images
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    player = pygame.transform.scale(player, (100, 100))

    # Print images
    screen.blit(background, (0, 0))
    screen.blit(player, (200, 150))

    pygame.display.update()

def initLevel(level):
    global myLevel
    myLevel = Level(level)

    drawLevel(myLevel.getFrontMatrix)
    #drawLevel(myLevel.getBackMatrix)

    global gotKey
    gotKey = False
    global leftover_moves
    leftover_moves = myLevel.moves

current_level = 1
initLevel(current_level)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r or leftover_moves == 0:
                initLevel(current_level)