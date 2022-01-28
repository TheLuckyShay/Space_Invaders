from Colors import COLORS
import pygame
import random
from pygame.constants import (
    K_DOWN,
    K_UP,
    K_LEFT,
    K_RIGHT,
    K_SPACE,
)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        #make the ship a random color (later add shop for them)
        self.surf = list(COLORS.values())[random.randint(0,1)]
        self.surf = self.surf.convert()
        
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2 - self.surf.get_width()/2, SCREEN_HEIGHT/2))
        self.shootDelay = 20
        self.shootTimer = 0
        self.speed = 6

    def shoot(self):
        bullet = Bullet((self.rect.centerx, self.rect.centery - (self.surf.get_height()/2)))
        return bullet
    def update(self, keyPresses):
        self.shootTimer += 1
        if keyPresses[K_UP]:
            self.rect.move_ip(0, -self.speed)
        if keyPresses[K_DOWN]:
            self.rect.move_ip(0, self.speed)
        if keyPresses[K_LEFT]:
            self.rect.move_ip(-self.speed, 0)
        if keyPresses[K_RIGHT]:
            self.rect.move_ip(self.speed, 0)
        if keyPresses[K_SPACE]:
            if self.shootTimer > self.shootDelay:
                self.shootTimer = 0
                return self.shoot()
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.surf = pygame.Surface((5,7))
        self.surf.fill((255,255,255))
        self.rect = self.surf.get_rect(center = pos)
        self.speed = 7

    def update(self):
        self.rect.move_ip(0, -self.speed)
        if self.rect.bottom < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super(Enemy, self).__init__()
        self.surf = self.surf = pygame.image.load("./assets/Asteroid_1.png").convert()
        self.rect = self.surf.get_rect(center = (random.randint(0, SCREEN_WIDTH), 0 - random.randint(20, 100)))
        self.speedy = random.randint(5, 9)
        self.speedx = int(random.randint(-4, 4)/2)

    def update(self):
        self.rect.move_ip(self.speedx, self.speedy)
        if self.rect.top > SCREEN_HEIGHT:
            self.kill()

