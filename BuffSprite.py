import pygame

from Player import Player

class BuffSprite(pygame.sprite.Sprite):

    def __init__(self, x: int, y: int, texture: str, size: tuple, speed: int, player: Player):
        super().__init__()

        self.image = pygame.transform.scale(pygame.image.load(texture), size)

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = speed
        self.player = player

    def draw(self, screen:pygame.display):
        screen.blit(self.image, self.rect)

    def activate(self):
        pass

    def update(self):
        self.rect.y += self.speed