import pygame, sys
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((640, 480))

rect = pygame.Rect(0, 0, 100, 100)
surf = pygame.Surface(rect.size).convert_alpha()
pygame.draw.rect(surf, (255, 0, 0), rect, 5)

# get new surface rotated 45°
rotated_surf = pygame.transform.rotate(surf, 45)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # blit rotated surface to screen at x=50, y=50
    screen.fill((0, 0, 0))
    screen.blit(rotated_surf, (50, 50))
    pygame.display.flip()