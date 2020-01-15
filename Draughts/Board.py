import pygame as pg
from Checker import Checker

class Board:
    def __init__(self, screen, squareSize):
        self.SIZE = 8
        self.checkers = []
        self.screen = screen
        self.SQUARE_SIZE = squareSize

    def setBoard(self, player1, player2):
        for x in range(1, self.SIZE, 2):
            # player 1
            self.checkers.append(Checker(x, 0, player1))
            self.checkers.append(Checker(x - 1, 1, player1))
            self.checkers.append(Checker(x, 2, player1))
            # player 2
            self.checkers.append(Checker(x - 1, 5, player2))
            self.checkers.append(Checker(x, 6, player2))
            self.checkers.append(Checker(x - 1, 7, player2))

    def draw(self):
        for checker in self.checkers:
            pg.draw.circle(self.screen, 
                           checker.player.color, 
                           (int(self.SQUARE_SIZE / 2 + checker.posX * self.SQUARE_SIZE), int(self.SQUARE_SIZE / 2 + checker.posY * self.SQUARE_SIZE)), 
                           checker.radius)

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

    def removeChecker(self, checker):
        self.checkers.remove(checker)

    def highlightChecker(self, checker):
        if checker is not None:
            pg.draw.circle(self.screen, 
                           (255,255,0), 
                           (int(self.SQUARE_SIZE / 2 + checker.posX * self.SQUARE_SIZE), int(self.SQUARE_SIZE / 2 + checker.posY * self.SQUARE_SIZE)), 
                           checker.radius, 3)
