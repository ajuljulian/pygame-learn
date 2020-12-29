import random
import pygame, sys
from pygame.locals import *
from vector import Vec2d

WIDTH, HEIGHT = 1280, 720

class Liquid:

    def __init__(self, x, y, w, h, c):
        
        super().__init__()

        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.c = c # coefficient of drag
    
    def display(self):
        pygame.draw.rect(screen, AQUA, (self.x, self.y, self.w, self.h))

class Mover:
    
    def __init__(self, location, mass, color):

        super().__init__()

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
    
    def is_inside(self, liquid):
        if self.location.x > liquid.x and self.location.x < liquid.x + liquid.w and \
            self.location.y > liquid.y and self.location.y < liquid.y + liquid.h:
            return True
        return False
    
    def get_drag(self, liquid):
        speed = self.velocity.get_length()
        drag_magnitude = liquid.c * speed * speed
        drag = self.velocity.normalized() * -1 * drag_magnitude
        return drag


pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.display.set_caption('Fluid Resistance')

GRAY_50 = (33, 33, 33, 50)
AQUA = (0, 255, 255)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

liquid = Liquid(0, HEIGHT/2, WIDTH, HEIGHT/2, 0.1)

NUM_MOVERS = 25

movers = []
for _ in range(NUM_MOVERS):
    color = GRAY_50
    random_location = Vec2d(random.randint(0, WIDTH), random.randint(0, HEIGHT/20))
    random_mass = random.uniform(0.5, 4)
    movers.append(Mover(random_location, random_mass, color))

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    liquid.display()

    for mover in movers:
        
        if mover.is_inside(liquid):
            drag = mover.get_drag(liquid)
            mover.apply_force(drag)

        m = 0.1 * mover.mass
        gravity = Vec2d(0, m)
        mover.apply_force(gravity)
        mover.update()
        mover.display()
        mover.check_edges()

    pygame.display.update()
    fpsClock.tick(FPS)