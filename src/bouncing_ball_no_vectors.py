'''
Bouncing ball without vectors.
'''
import pygame, sys
from pygame.locals import *

WIDTH, HEIGHT = 640, 360

pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.display.set_caption('Bouncing Ball')

GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

x = 100
y = 100
xspeed = 1
yspeed = 3.3

while True:
    DISPLAYSURF.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    x = x + xspeed
    y = y + yspeed
    
    if x > WIDTH or x < 0:
        xspeed = xspeed * -1
    if y > HEIGHT or y < 0:
        yspeed = yspeed * -1

    pygame.draw.circle(DISPLAYSURF, GRAY, (x, y), 16, 0)
    pygame.display.update()
    fpsClock.tick(FPS)