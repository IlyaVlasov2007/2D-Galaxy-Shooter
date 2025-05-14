import pygame

from GameSprite import GameSprite

class Enemy(GameSprite):

    def __init__(self, texture: str, x: int, y: int, speed: int, health: float, size: tuple = (65, 65)):
        super().__init__(texture, x, y, speed, size=size)

        self.health = health
        self.max_health = health

    def draw_hp(self, screen):
        pygame.draw.line(screen, (255, 0, 0), start_pos=(self.rect.x, self.rect.y-20),
                                                    end_pos=(self.rect.x+self.rect.width,
                                                             self.rect.y-20), width=10)

        pygame.draw.line(screen, (0, 255, 0), start_pos=(self.rect.x, self.rect.y - 20),
                                                    end_pos=(self.rect.x + (self.health/self.max_health) * self.rect.width,
                                                    self.rect.y - 20), width=10)

    def update(self):
        self.rect.y += self.speed