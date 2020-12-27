import random
import pygame, sys
from pygame.locals import *
from vector import Vec2d

WIDTH, HEIGHT = 640, 360

class Mover:
    def __init__(self):
        self.location = Vec2d(random.randint(0, WIDTH), random.randint(0, HEIGHT))
        self.velocity = Vec2d(0, 0)
        self.acceleration = Vec2d(0, 0)
        self.topspeed = 9
        self.mass = 1

    def apply_force(self, force):
        f = force / self.mass
        self.acceleration += f

    def update(self):
        self.velocity += self.acceleration
        self.location += self.velocity
        self.acceleration *= 0
    '''    
    def display(self):
        pygame.draw.circle(screen, GRAY, (self.location.x, self.location.y), 16, 2)
    '''
    def draw_circle_alpha(self, surface, color, radius):
        target_rect = pygame.Rect((self.location.x, self.location.y), (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape_surf, color, (radius, radius), radius)
        surface.blit(shape_surf, target_rect)
        # There has to be a better way of drawing a border around a transparent shape.
        pygame.draw.circle(screen, GRAY, (self.location.x, self.location.y), radius, 2)
        

    
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

movers = [Mover() for _ in range(20)]

pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.display.set_caption('Bouncing Balls with Force')

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
    wind = Vec2d(0.01, 0)
    gravity = Vec2d(0, 0.1)

    for mover in movers:
        mover.apply_force(wind)
        mover.apply_force(gravity)
        mover.update()
        #mover.display()
        mover.draw_circle_alpha(screen, GRAY, 16)
        mover.check_edges()

    pygame.display.update()
    fpsClock.tick(FPS)