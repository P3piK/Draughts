class Checker:
    def __init__(self, x, y, player):
        self.posX = x
        self.posY = y
        self.player = player
        self.radius = 15

    def isMoveAvailable(self, dest):
        ret = False
        if self.player == 0:
            if dest == (self.posX + 1, self.posY + 1) or dest == (self.posX - 1, self.posY + 1):
                ret = True
        else:
            if dest == (self.posX + 1, self.posY - 1) or dest == (self.posX - 1, self.posY - 1):
                ret = True
        return ret

    def move(self, dest):
        if self.isMoveAvailable(dest):
            self.posX = dest[0]
            self.posY = dest[1]
