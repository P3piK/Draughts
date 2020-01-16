import pygame as pg
import os
from Board import Board
from Checker import Checker
from Player import Player

main_dir = os.path.split(os.path.abspath(__file__))[0]

SCREENSIZE = 305
SQUARESIZE = SCREENSIZE / 8

def load_image(file):
    file = os.path.join(main_dir, "data", file)
    try:
        surface = pg.image.load(file)
    except pg.error:
        raise SystemExit('Could not load image "%s" %s' % (file, pg.get_error()))
    return surface.convert()

def nextTurn(playerId):
    return playerId % 2 + 1

# Initialize pygame
screen = pg.display.set_mode((SCREENSIZE, SCREENSIZE))

background_image = load_image("board.png")
pg.font.init()
font = pg.font.SysFont("Arial", 22)

running = True
player1 = Player(1, (255,0,0))
player2 = Player(2, (0,0,255))
board = Board(screen, SQUARESIZE)
board.setBoard(player1, player2)

checkerSelected = None
dest = None
checker = None
draw = True
playerTurn = 1
playerColorDict = {1:"RED", 2:"BLUE"}

# Main loop
while running:
    # Input events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        # Mouse events
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0] == True:
                mouse_pos = pg.mouse.get_pos()
                # select checker at first
                if checkerSelected is None:
                    checkerSelected = (int(mouse_pos[0] / SQUARESIZE), int(mouse_pos[1] / SQUARESIZE))
                # then select destination square
                else:
                    dest = (int(mouse_pos[0] / SQUARESIZE), int(mouse_pos[1] / SQUARESIZE))
            elif pg.mouse.get_pressed()[2] == True:
                checkerSelected = None
                checker = None
                draw = True

    # Player's move
    if checkerSelected is not None:
        checker = board.getChecker(checkerSelected)
        if checker is not None and checker.player.id == playerTurn:
            draw = True
            if dest is not None and not board.isChecker(dest):
                checkerTaken = board.getChecker(((checkerSelected[0] + dest[0]) / 2, (checkerSelected[1] + dest[1]) / 2))   # checker between current position and destination
                if checker.isMoveAvailable(dest):
                    checker.move(dest)
                    playerTurn = nextTurn(playerTurn)
                elif checkerTaken is not None and checker.isJumpAvailable(dest) and checker.player != checkerTaken.player:
                    checker.jump(dest)
                    board.removeChecker(checkerTaken)
                    playerTurn = nextTurn(playerTurn)
                    running = board.isAnyCheckerLeft()
                dest = None
                checkerSelected = None
                checker = None
                print(playerTurn)
        else:
            checkerSelected = None

    # Drawing
    if draw:
        screen.blit(background_image, [0, 0])
        board.draw()
        board.highlightChecker(checker)
        screen.blit(font.render("Player {0} turn".format(playerColorDict[playerTurn]), True, (0,0,0)), [100,5])
        pg.display.flip()
        draw = False
