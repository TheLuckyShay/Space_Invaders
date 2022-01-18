import pygame
from Players import Bullet, Player, Enemy
from pygame.constants import (
    QUIT,
    K_ESCAPE,
    KEYDOWN,
)

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650

class screenShow():
    def __init__(self):
        self.screen = "game"
        self.level = 1
    
    def level1(self, screen, clock):
        player = Player()

        ADDENEMY = pygame.USEREVENT + 1
        enemySpawnSpeed = 500
        pygame.time.set_timer(ADDENEMY, enemySpawnSpeed)

        enemies = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        all_sprites = pygame.sprite.Group()
        all_sprites.add(player)
        all_sprites.add(bullets)
        score = 0
        pygame.display.flip()

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                elif event.type == ADDENEMY:
                    if len(enemies) < 30:
                        enemy = Enemy()
                        enemies.add(enemy)
                        all_sprites.add(enemy)
                        score += 1
            keyPresses = pygame.key.get_pressed()
            screen.fill((0,0,0))
            maybeBullet = player.update(keyPresses)
            if isinstance(maybeBullet, Bullet):
                bullets.add(maybeBullet)
                all_sprites.add(maybeBullet)

            for entity in all_sprites:
                screen.blit(entity.surf, entity.rect)
            
            bullets.update()
            enemies.update()

            if pygame.sprite.spritecollideany(player, enemies):
                player.kill()
                running = False
            for enemy in enemies:
                for bullet in bullets:
                    if pygame.sprite.collide_rect(enemy, bullet):
                        score += 5
                        enemy.kill()
                        bullet.kill()
            if score%5 == 0 and enemySpawnSpeed-30 > 0:
                enemySpawnSpeed -= 30
                pygame.time.set_timer(ADDENEMY, enemySpawnSpeed)
                score += 1
                print(enemySpawnSpeed)

            font = pygame.font.Font(None, 74)
            text = font.render(str(score), 1, (255,255,255))
            screen.blit(text, (SCREEN_WIDTH - 20 - text.get_width(),20))
            pygame.display.flip()
            clock.tick(90)
