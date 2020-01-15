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

# Initialize pygame
screen = pg.display.set_mode((SCREENSIZE, SCREENSIZE))

background_image = load_image("board.png")

finished = False
player1 = Player(1, (255,0,0))
player2 = Player(2, (0,0,255))
board = Board(screen, SQUARESIZE)
board.setBoard(player1, player2)

checkerSelected = None
dest = None
checker = None
draw = True

# Main loop
while not finished:
    # Input events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True
        # Mouse events
        if event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed()[0] == True:
                mouse_pos = pg.mouse.get_pos()
                # select checker at first
                if checkerSelected is None:
                    checkerSelected = (int(mouse_pos[0] / SQUARESIZE), int(mouse_pos[1] / SQUARESIZE))
                    print(checkerSelected)
                # then select destination square
                else:
                    dest = (int(mouse_pos[0] / SQUARESIZE), int(mouse_pos[1] / SQUARESIZE))
                    print(dest)

    # Player's move
    if checkerSelected is not None:
        checker = board.getChecker(checkerSelected)
        if checker is not None:
            draw = True
            if dest is not None and not board.isChecker(dest):
                checkerTaken = board.getChecker(((checkerSelected[0] + dest[0]) / 2, (checkerSelected[1] + dest[1]) / 2))   # checker between current position and destination
                if checker.isMoveAvailable(dest):
                    checker.move(dest)
                elif checkerTaken is not None and checker.isJumpAvailable(dest) and checker.player != checkerTaken.player:
                    checker.jump(dest)
                    board.removeChecker(checkerTaken)
                dest = None
                checkerSelected = None
                checker = None
        else:
            checkerSelected = None

    # Drawing
    if draw:
        screen.blit(background_image, [0, 0])
        board.draw()
        board.highlightChecker(checker)
        pg.display.flip()
        draw = False
