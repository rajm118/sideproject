import pygame as pg,sys
from pygame.locals import *
import time
#initialize global variables
XO = 'x'
winner = None
draw = False
width = 500
height = 500
white = (255, 255, 255)
line_color = (10,10,10) #black
#TicTacToe 3x3 board
#ititialize the board with none as values
TTT = [[None]*3,[None]*3,[None]*3]
pg.init()
fps = 60
CLOCK = pg.time.Clock()
screen = pg.display.set_mode((width, height+100),0,32)
pg.display.set_caption("Tic Tac Toe")


def game_opening():
    screen.blit(opening, (0, 0))
    pg.display.update()
    time.sleep(1)
    screen.fill(white)
    # Drawing vertical lines
    pg.draw.line(screen, line_color, (width / 3, 0), (width / 3, height), 7)
    pg.draw.line(screen, line_color, (width / 3 * 2, 0), (width / 3 * 2, height), 7)
    # Drawing horizontal lines
    pg.draw.line(screen, line_color, (0, height / 3), (width, height / 3), 7)
    pg.draw.line(screen, line_color, (0, height / 3 * 2), (width, height / 3 * 2), 7)
    draw_status()

def draw_status():
     global draw
     if winner is None:

         message = XO.upper() + "'s Turn"
     else:
         message = winner.upper() + " won!"
     if draw:
         message = 'Game Draw!'
     font = pg.font.Font(None, 30)
     text = font.render(message, 1, (255, 255, 255))
# copy the rendered message onto the board
     screen.fill ((0, 0, 0), (0, 400, 500, 100))
     text_rect = text.get_rect(center=(width/2, 500-50))
     screen.blit(text, text_rect)
     pg.display.update()