import pygame
from Screens import *
from pygame.constants import (
    QUIT,
    K_ESCAPE,
    KEYDOWN,
)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
pygame.init()
clock = pygame.time.Clock()
level = screenShow()
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
level.level1(screen, clock)
pygame.quit()