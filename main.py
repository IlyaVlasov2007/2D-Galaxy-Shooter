import pygame
import sys

from Player import Player
from EnemySpawner import EnemySpawner
from BuffSpawner import BuffSpawner
from Explosion import Explosion

FPS = 60
root = pygame.display.set_mode((700, 500))
pygame.display.set_caption("Galaxy Shooter")

icon = pygame.image.load("Assets/ico.ico")

pygame.display.set_icon(icon)

background = pygame.transform.scale(pygame.image.load("Assets/Textures/background.jpg"),(700, 500))
player = Player(texture = "Assets/Textures/player.png",
                shielded_texture="Assets/Textures/shielded_player.png",
                x = 300, y = 400, speed = 10, size = (65, 95))

# Bullets and Enemies Groups
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
buffs = pygame.sprite.Group()
explosions = pygame.sprite.Group()

# Create Spawners
enemy_spawner = EnemySpawner(group = enemies)
buff_spawner = BuffSpawner(screen = root, player = player, group = buffs)

# Different Labels
pygame.font.init()
font = pygame.font.SysFont('Arial', 30)
score_label = font.render(f'Score: {player.score}', True, (255, 255, 255))
missing_score_label = font.render(f'Missing Score: {player.missing_score}', True, (255, 255, 255))
lose_label = font.render('You Lose!', True, (255, 0, 0))
damage_label = font.render(f"Damage: {player.damage}", True, (255, 0, 0))

while True:
    root.blit(background, (0, 0))

    for event in pygame.event.get():

        # Exit
        if event.type == pygame.QUIT:
            sys.exit(0)

        # Shoot
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot(group = bullets)

# Collide Player -> Enemy
    for enemy in enemies:
        enemy.draw_hp(screen = root)
        if pygame.sprite.collide_rect(player, enemy):
            if not player.is_shield:
                explosions.add(Explosion(player.rect.x, player.rect.y))
                player.kill()
                player.lose = True

                enemy_spawner.is_active = False
                buff_spawner.is_active = False
                break
            else:
                player.unset_shield()

                enemy.kill()
                del enemy
                break

        if enemy.rect.y > (player.rect.y + 95):
            player.missing_score += 1
            missing_score_label = font.render(f'Missing Score: {player.missing_score}', True, (255, 255, 255))

            enemy.kill()
            del enemy

# Collide Enemy -> Bullet
    for bullet in bullets:
        for enemy in enemies:
            if pygame.sprite.collide_rect(enemy, bullet):
                enemy.health -= player.damage

                if enemy.health <= 0:
                    player.score += 1
                    score_label = font.render(f'Score: {player.score}', True, (255, 255, 255))

                    explosions.add(Explosion(enemy.rect.x, enemy.rect.y))

                    enemy.kill()
                    del enemy

                bullet.kill()

                del bullet
                break
        continue

    for buff in buffs:
        if pygame.sprite.collide_rect(player, buff):
            buff.activate()

            buff.kill()
            del buff
            break

        if buff.rect.y > (player.rect.y + 95):
            buff.kill()
            del buff

# Draw Objects
    if not player.lose:
        player.draw(root)
        bullets.draw(root)

    enemies.draw(root)
    buffs.draw(root)
    explosions.draw(root)

    root.blit(score_label, (5, 5))
    root.blit(missing_score_label, (5, 40))

    if player.missing_score >= 3:
        player.lose = True
        enemy_spawner.is_active = False
        buff_spawner.is_active = False

    if player.lose:
        root.blit(lose_label, (300, 200))

# Update Objects
    player.update()
    bullets.update()
    damage_label = font.render(f"Damage: {player.damage}", True, (255, 0, 0))
    root.blit(damage_label, (5, 75))

    enemy_spawner.update()
    buff_spawner.update()
    explosions.update()

    pygame.time.Clock().tick(FPS)
    pygame.display.update()