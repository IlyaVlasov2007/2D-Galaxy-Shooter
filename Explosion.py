import pygame

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        death_frame = ["Assets/Animations/Enemy Death/1.png",
                       "Assets/Animations/Enemy Death/2.png",
                       "Assets/Animations/Enemy Death/3.png",
                       "Assets/Animations/Enemy Death/4.png",
                       "Assets/Animations/Enemy Death/5.png",
                       "Assets/Animations/Enemy Death/6.png",
                       "Assets/Animations/Enemy Death/7.png",
                       "Assets/Animations/Enemy Death/8.png",
                       "Assets/Animations/Enemy Death/9.png"]
        self.anim = []

        for frame in death_frame:
            self.anim.append(pygame.transform.scale(pygame.image.load(frame), (95, 95)))

        self.image = self.anim[0]
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = x, y

        self.frame = 0
        self.last_update = pygame.time.get_ticks()
        self.frame_rate = 20

    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1
            if self.frame == len(self.anim):
                self.kill()
                del self
                return

            self.image = self.anim[self.frame]