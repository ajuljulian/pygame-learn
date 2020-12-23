import math
import pygame, sys
from pygame.locals import *

WIDTH, HEIGHT = 500, 400

pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()

DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.display.set_caption('Pulsate')

GRAY = (128, 128, 128)
BLACK = (0, 0, 0)

period = 360
amplitude = 100

framecount = 0

while True:
    DISPLAYSURF.fill(GRAY)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    # sin(0) = 0, sin(pi/2) = 1, sin(pi) = 0, so this value oscillates between 0 and amplitude.
    sphere_radius = amplitude * math.sin(math.pi * (framecount % period)/period)
    pygame.draw.circle(DISPLAYSURF, BLACK, (WIDTH/2, HEIGHT/2), sphere_radius, 0)
    pygame.display.update()
    framecount += 1
    fpsClock.tick(FPS)
