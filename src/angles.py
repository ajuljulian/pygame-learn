import pygame, sys
from pygame.locals import *

# set up colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

pygame.init()

FPS = 60

fpsClock = pygame.time.Clock()

width, height = 640, 360

screen = pygame.display.set_mode((width, height), 0, 32)

pygame.display.set_caption('Angles')

rect = pygame.Rect(0, 0, 100, 2)
surf = pygame.Surface(rect.size).convert_alpha()
pygame.draw.rect(surf, BLACK, rect)

# get new surface rotated 45°
# rotated_surf = pygame.transform.rotate(surf, 90)

framecount = 0

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(WHITE)
    old_center = rect.center
    rotated_surf = pygame.transform.rotate(surf, framecount % 360)
    new_rect = rotated_surf.get_rect()
    new_rect.center = old_center
    #screen.blit(rotated_surf, (width/2 - 50, height/2))
    screen.blit(rotated_surf, new_rect)
    #pygame.display.flip()
    pygame.display.update()
    framecount += 1
    fpsClock.tick(FPS)
