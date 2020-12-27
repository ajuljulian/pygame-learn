'''
Movers accelerating towards mouse
'''
import random
import pygame, sys
from pygame.locals import *
from vector import Vec2d

WIDTH, HEIGHT = 640, 360

class Mover:
    def __init__(self):
        self.location = Vec2d(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.velocity = Vec2d(0, 0)
        self.topspeed = 9

    def update(self, mouse_x, mouse_y):
        mouse_loc = Vec2d(mouse_x, mouse_y)
        dir = mouse_loc - self.location
        dir = dir.normalized()
        dir *= 0.5

        self.acceleration = dir
        self.velocity += self.acceleration

        if self.velocity.length > self.topspeed:
            self.velocity.length = self.topspeed

        self.location += self.velocity

    def display(self):
        pygame.draw.circle(screen, GRAY, (self.location.x, self.location.y), 16, 2)

    def draw_circle_alpha(self, surface, color, radius):
        target_rect = pygame.Rect((self.location.x, self.location.y), (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape_surf, color, (radius, radius), radius)
        surface.blit(shape_surf, target_rect)
        # There has to be a better way of drawing a border around a transparent shape.
        pygame.draw.circle(screen, GRAY, (self.location.x, self.location.y), radius, 2)
        

    
    def check_edges(self):
        if self.location.x > WIDTH:
            self.location.x = 0
        elif self.location.x < 0:
            self.location.x = WIDTH

        if self.location.y > HEIGHT:
            self.location.y = 0
        elif self.location.y < 0:
            self.location.y = HEIGHT 

movers = [Mover() for _ in range(20)]

pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.display.set_caption('Movers Accelerating Towards Mouse')

GRAY = (128, 128, 128, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    for mover in movers:
        mover.update(mouse_x, mouse_y)
        mover.check_edges()
        #mover.display()
        mover.draw_circle_alpha(screen, GRAY, 16)

    pygame.display.update()
    fpsClock.tick(FPS)