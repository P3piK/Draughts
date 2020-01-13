import pygame as pg
from Checker import Checker

class Board:
    def __init__(self):
        self.size = 8
        self.checkers = []

    def setBoard(self):
        for x in range(1, self.size, 2):
            # player 1
            self.checkers.append(Checker(x, 0, 0))
            self.checkers.append(Checker(x - 1, 1, 0))
            self.checkers.append(Checker(x, 2, 0))
            # player 2
            self.checkers.append(Checker(x - 1, 5, 1))
            self.checkers.append(Checker(x, 6, 1))
            self.checkers.append(Checker(x - 1, 7, 1))

    def draw(self, screen):
        for checker in self.checkers:
            color = (255 * checker.player, 255 * checker.player, 255 * checker.player)
            pg.draw.circle(screen, color, (19 + checker.posX * 38, 19 + checker.posY * 38), checker.radius)

    def isChecker(self, pos):
        for x in self.checkers:
            if x.posX == pos[0] and x.posY == pos[1]:
                return True
        return False

    def getChecker(self, pos):
        for x in self.checkers:
            if x.posX == pos[0] and x.posY == pos[1]:
                return x
        return None

