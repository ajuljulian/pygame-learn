import random
import pygame, sys
from pygame.locals import *
from vector import Vec2d

WIDTH, HEIGHT = 1280, 720

class Mover:
    def __init__(self, location, mass, color):
        super().__init__()
        self.location = location
        self.mass = mass
        self.G = 0.4
        self.color = color
        self.velocity = Vec2d(0, 0)
        self.acceleration = Vec2d(0, 0)
        self.topspeed = 9

    def attract(self, other):
        force = self.location - other.location
        distance = force.length
        distance = self._constrain(distance, 5.0, 10.0)
        force = force.normalized()
        strength = (self.G * self.mass * other.mass) / (distance**2)
        force = force * strength
        return force

    def apply_force(self, force):
        acceleration = force / self.mass
        self.acceleration += acceleration

    def update(self):
        self.velocity += self.acceleration
        self.location += self.velocity
        self.acceleration *= 0
      
    def display(self):
        radius = self.mass * 4
        pygame.draw.circle(screen, self.color, (self.location.x, self.location.y), radius, 2)
        target_rect = pygame.Rect((self.location.x, self.location.y), (0, 0)).inflate((radius * 2, radius * 2))
        shape_surf = pygame.Surface(target_rect.size, pygame.SRCALPHA)
        pygame.draw.circle(shape_surf, self.color, (radius, radius), radius)
        screen.blit(shape_surf, target_rect)
    
    def _constrain(self, distance, min_distance, max_distance):
        if distance < min_distance: 
            return min_distance
        elif distance > max_distance:
            return max_distance
        else:
            return distance

class Attractor:
    def __init__(self, color):
        super().__init__()
        self.location = Vec2d(WIDTH/2, HEIGHT/2)
        self.mass = 40
        self.G = 0.4
        self.color = color

    def attract(self, mover):
        force = self.location - mover.location
        distance = force.length
        distance = self._constrain(distance, 5.0, 10.0)
        force = force.normalized()
        strength = (self.G * self.mass * mover.mass) / (distance**2)
        force = force * strength
        return force
    
    def display(self):
        radius = self.mass
        pygame.draw.circle(screen, self.color, (self.location.x, self.location.y), radius, 0)

    def _constrain(self, distance, min_distance, max_distance):
        if distance < min_distance: 
            return min_distance
        elif distance > max_distance:
            return max_distance
        else:
            return distance


pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT), 0, 32)

pygame.display.set_caption('Mover and Attractor')

GRAY_50 = (33, 33, 33, 50)
AQUA = (0, 255, 255)
ORANGE = (255, 191, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

NUM_MOVERS = 10

movers = []
for _ in range(NUM_MOVERS):
    color = GRAY_50
    random_location = Vec2d(random.randint(0, WIDTH), random.randint(0, HEIGHT))
    random_mass = random.uniform(4, 4)
    movers.append(Mover(random_location, random_mass, color))

attractor = Attractor(ORANGE)

while True:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    attractor.display()

    for i, mover1 in enumerate(movers):
        for j, mover2 in enumerate(movers):
            if i != j:
                force = mover1.attract(mover2)
                mover1.apply_force(force)

        force = attractor.attract(mover1)
        mover1.apply_force(force)
        mover1.update()
        mover1.display()

    pygame.display.update()
    fpsClock.tick(FPS)