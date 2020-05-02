import pygame

pygame.init()
# create screen use tuple to initialize the size of the screen
screen = pygame.display.set_mode((800, 600))

# title and icon
pygame.display.set_caption("Space Invaders")
# create the variable to load the image and then use the image
icon = pygame.image.load('technology.png')
pygame.display.set_icon(icon)

#initialzing the player
playerImg= pygame.image.load('player.png')
playerX = 370
playerY = 400

def player():
    screen.blit(playerImg,(playerX,playerY))


running = True
while running:
    screen.fill((0, 0, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()
    #necessary in order to update the screen else it will show previous data only
    pygame.display.update()