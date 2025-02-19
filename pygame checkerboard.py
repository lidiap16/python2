# Author: lidia
# Date: Feb 19
# Purpose: Further pygame activities

import pygame, sys
from pygame.locals import *

# start the pygame engine
pygame.init()

# create a 400x400 window
window = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Chequer Board')

# define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

window.fill(WHITE) # paint the window white
y = 0
y2 = 50
# Draw Row 1
for i in range(0,5):
    pygame.draw.rect(window, BLACK, (0,   y, 50, 50))
    pygame.draw.rect(window, BLACK, (100, y, 50, 50))
    pygame.draw.rect(window, BLACK, (200, y, 50, 50))
    pygame.draw.rect(window, BLACK, (300, y, 50, 50))
    y = y + 100
    pygame.draw.rect(window, BLACK, (50,  y2, 50, 50))
    pygame.draw.rect(window, BLACK, (150, y2, 50, 50))
    pygame.draw.rect(window, BLACK, (250, y2, 50, 50))
    pygame.draw.rect(window, BLACK, (350, y2, 50, 50))
    y2 = y2 + 100

pygame.display.update()

# run the game loop
while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
