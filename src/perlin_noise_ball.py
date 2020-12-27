'''
Perlin noise ball
'''
import pygame, sys
from perlin_noise import PerlinNoise
from pygame.locals import *

class Ball:
    def __init__(self):
        self.x = SCREEN_WIDTH / 2
        self.y = SCREEN_HEIGHT / 2
        self.tx = 0
        self.ty = 0
        self.noiseX = PerlinNoise(octaves=10, seed=1)
        self.noiseY = PerlinNoise(octaves=10, seed=2)

    def draw(self):
       pygame.draw.circle(screen, GRAY, (self.x, self.y), 16, 0) 

    def step(self):
        self.x += self.noiseX((self.tx % 100)/100) * 10
        self.y += self.noiseY((self.ty % 100)/100) * 10
        self.tx += 0.25
        self.ty += 0.25

SCREEN_WIDTH, SCREEN_HEIGHT = 640, 360

pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

pygame.display.set_caption('Perlin Ball')

GRAY = (128, 128, 128)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

ball = Ball()

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ball.draw()
    ball.step()
    pygame.display.update()
    fpsClock.tick(FPS)
    