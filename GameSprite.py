import pygame

class GameSprite(pygame.sprite.Sprite):
    def __init__(self, texture:str, x:int, y:int, speed:int, size:tuple = (65, 65)):
        super().__init__()

        self.speed = speed
        self.image = pygame.transform.scale(pygame.image.load(texture), size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        pass