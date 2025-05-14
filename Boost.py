from BuffSprite import BuffSprite

class Boost(BuffSprite):

    def activate(self):
        self.player.damage += 2