import random
import pygame

from Enemy import Enemy

pygame.font.init()
font = pygame.font.SysFont('Arial', 30)

class EnemySpawner:

    def __init__(self, group:pygame.sprite.Group):
        self.cooldown: int = 0
        self.group = group
        self.is_active = True
        self.start_hp: float = 0.5

    def spawn(self):
            self.group.add(Enemy(texture = "Assets/Textures/enemy.png",
                                 x = random.randint(0, 605),
                                 y = random.randint(-95, -65),
                                 speed = random.randint(2, 4),
                                 health = self.start_hp,
                                 size = (95, 65)))

            self.cooldown = 60

    def update(self):
        self.cooldown -= 1
        self.start_hp += 0.001

        if self.is_active:
            if self.cooldown <= 0:
                self.spawn()
            self.group.update()