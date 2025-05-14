import pygame

from GameSprite import GameSprite
from Bullet import Bullet

from random import randint

CONTROL = [[pygame.K_UP, pygame.K_w],
           [pygame.K_DOWN, pygame.K_s],
           [pygame.K_LEFT, pygame.K_a],
           [pygame.K_RIGHT, pygame.K_d]]

BEAMS = ["Assets/Textures/beam_blue.png",
         "Assets/Textures/beam_pink.png",
         "Assets/Textures/beam_red.png",
         "Assets/Textures/beam_yellow.png"]

class Player(GameSprite):

    def __init__(self, texture: str, shielded_texture: str, x:int, y:int, speed:int, size:tuple = (65, 65)):
        super().__init__(texture, x, y, speed, size = size)

        self.score: int = 0
        self.missing_score: int = 0
        self.damage: float = 1
        self.is_shield: bool = False
        self.lose = False
        self.cooldown: int = 0

        self.shield_texture = shielded_texture
        self.unshield_texture = texture

    def shoot(self, group:pygame.sprite.Group):
        if not self.lose and self.cooldown <= 0:
            group.add(Bullet(texture = BEAMS[randint(0, 3)],
                             x = self.rect.x + 28, y = self.rect.y - 20,
                             speed = 3,
                             size=(12, 30)))
            self.cooldown = 20

    def set_shield(self):
        self.image = pygame.transform.scale(pygame.image.load(self.shield_texture), (self.rect.width, self.rect.height))
        self.is_shield = True

    def unset_shield(self):
        self.image = pygame.transform.scale(pygame.image.load(self.unshield_texture), (self.rect.width, self.rect.height))
        self.is_shield = False

    def left(self):
        self.rect.x -= self.speed

    def right(self):
        self.rect.x += self.speed

    def update(self):
        keys = pygame.key.get_pressed()

        if (keys[CONTROL[2][0]] or keys[CONTROL[2][1]]) and self.rect.x > 20: self.left()
        if (keys[CONTROL[3][0]] or keys[CONTROL[3][1]]) and self.rect.x < 615: self.right()

        if self.cooldown >= 0:
            self.cooldown -= 1