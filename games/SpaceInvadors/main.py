import pygame
import random

pygame.init()
# create screen use tuple to initialize the size of the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
# create the variable to load the image and then use the image
icon = pygame.image.load('technology.png')
pygame.display.set_icon(icon)
enemyImg = pygame.image.load('enemy.png')
enemyX = random.randint(0, 750)
enemyY = random.randint(50, 200)

# initialzing the player
playerImg = pygame.image.load('player.png')
# initialize the position
playerX = 370
playerY = 400
playerX_change = 0.0
playerY_change = 0.1


def player(x, y):
    screen.blit(playerImg, (x, y))


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def enemy_movement(enemyX, enemyY):
    enemy_change = 0.3
    print(enemyX)
    enemyX += enemy_change
    if enemyX >= 750:
        enemyY += 32
        enemyX = 50
    elif enemyX < 32:
        enemyY += 32
    print("enemy " , enemyX)
    return enemyX,enemyY

def player_movemnet(player_X,player_Y):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            print("Left arrow pressed")
            playerX_change = -0.1

        if event.key == pygame.K_RIGHT:
            playerX_change = 0.1
            print("Right arrow pressed")
    if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
            print("Keystroke has been released ")
            playerX_change = 0


running = True
while running:
    screen.fill((0, 0, 255))
    enemy(enemyX, enemyY)
    enemyX,enemyY=enemy_movement(enemyX, enemyY)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # adding keystroke
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                print("Left arrow pressed")
                playerX_change = -0.1

            if event.key == pygame.K_RIGHT:
                playerX_change = 0.1
                print("Right arrow pressed")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                print("Keystroke has been released ")
                playerX_change = 0

    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 768:
        playerX = 768
    player(playerX, playerY)
    # necessary in order to update the screen else it will show previous data only
    pygame.display.update()
