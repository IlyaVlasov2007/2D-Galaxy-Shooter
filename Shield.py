from BuffSprite import BuffSprite

class Shield(BuffSprite):

    def activate(self):
        self.player.set_shield()
