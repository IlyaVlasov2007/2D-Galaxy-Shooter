import pygame
from random import randint

from Shield import Shield
from Boost import Boost
from Player import Player

class BuffSpawner:

    def __init__(self, screen: pygame.display, player: Player, group:pygame.sprite.Group):
        self.cooldown: int = 0 # 20 sec
        self.is_active = True

        self.screen = screen
        self.player = player
        self.group = group

    def spawn(self):
        var: int = randint(0, 1)
        if var == 0:
            self.group.add(Shield(x = randint(0, 605),
                                  y = randint(-95, -65),
                                  texture = "Assets/Textures/shield.png",
                                  size = (50, 50),
                                  speed = randint(5, 7),
                                  player = self.player))
        else:
            self.group.add(Boost(x = randint(0, 605),
                                 y = randint(-95, -65),
                                 texture = "Assets/Textures/boost.png",
                                 size = (50, 50),
                                 speed = randint(5, 7),
                                 player = self.player))

    def update(self):
        self.cooldown -= 1

        if self.is_active:
            if self.cooldown <= 0:
                self.spawn()
                self.cooldown = 420  # 7 sec
            self.group.update()