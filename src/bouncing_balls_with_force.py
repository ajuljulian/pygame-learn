import random
import pygame, sys
from pygame.locals import *
from vector import Vec2d

WIDTH, HEIGHT = 640, 360

class Mover:
    
    def __init__(self, location, mass, color):
        self.location = location
        self.mass = mass
        self.color = color
        self.velocity = Vec2d(0, 0)
        self.acceleration = Vec2d(0, 0)
        self.topspeed = 9

    def apply_force(self, force):
        acceleration = force / self.mass
        self.acceleration += acceleration

    def update(self):
        self.velocity += self.acceleration
        self.location += self.velocity
        self.acceleration *= 0
      
    def display(self):
        radius = self.mass * 8
        pygame.draw.circle(screen, self.color, (self.location.x, self.location.y), radius, 2)
        target_rect = pygame.Rect((self.location.x, self.location.y), (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape_surf, self.color, (radius, radius), radius)
        screen.blit(shape_surf, target_rect)
    
    def check_edges(self):
        if self.location.x > WIDTH:
            self.location.x = WIDTH
            self.velocity.x *= -1
        elif self.location.x < 0:
            self.location.x = 0
            self.location.x *= -1

        if self.location.y > HEIGHT:
            self.location.y = HEIGHT
            self.velocity.y *= -1
        elif self.location.y < 0:
            self.location.y = 0
            self.velocity.y *= -1 

GRAY_50 = (128, 128, 128, 50)
RED_50 = (255, 0, 0, 50)
GREEN_50 = (0, 255, 0, 50)
BLUE_50 = (0, 0, 255, 50)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

NUM_MOVERS = 50

movers = []
for _ in range(NUM_MOVERS):
    random_color = random.choice([GRAY_50, RED_50, GREEN_50, BLUE_50])
    random_location = Vec2d(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    random_mass = random.uniform(0.5, 4)
    movers.append(Mover(random_location, random_mass, random_color))

pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.display.set_caption('Bouncing Balls with Force')

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    wind = Vec2d(0.01, 0)
    gravity = Vec2d(0, 0.1)

    for mover in movers:
        mover.apply_force(wind)
        mover.apply_force(gravity)
        mover.update()
        mover.display()
        mover.check_edges()

    pygame.display.update()
    fpsClock.tick(FPS)