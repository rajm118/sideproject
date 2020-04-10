import pygame
from pygame.locals import (

    K_UP,

    K_DOWN,

    K_LEFT,

    K_RIGHT,

    K_ESCAPE,

    KEYDOWN,

    QUIT,

)
pygame.init()
carryOn = True
clock = pygame.time.Clock()
# Define some colors
BLACK = ( 0, 0, 0)
WHITE = ( 255, 255, 255)
GREEN = ( 0, 255, 0)
RED = ( 255, 0, 0)
size = (700, 700)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("My First Game")

while carryOn:
    # --- Main event loop
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            carryOn = False  # Flag that we are done so we exit this loop

    screen.fill(WHITE)
    pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)

    pygame.display.flip()
    SCREEN_WIDTH = 800

    SCREEN_HEIGHT = 600

    # Create the screen object

    # The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock.tick(50)
pygame.quit()