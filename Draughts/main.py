import pygame as pg
import os
from Board import Board
from Checker import Checker

main_dir = os.path.split(os.path.abspath(__file__))[0]

SCREENSIZE = 305
SQUARESIZE = SCREENSIZE / 8

def load_image(file):
    """ loads an image, prepares it for play
    """
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
board = Board()
board.setBoard()

checkerSelected = None
dest = None

# Main loop
while not finished:
    # Input events
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

        if event.type == pg.MOUSEBUTTONDOWN:
            # select checker with left mouse
            if pg.mouse.get_pressed()[0] == True:
                mouse_pos = pg.mouse.get_pos()
                checkerSelected = (int(mouse_pos[0] / SQUARESIZE), int(mouse_pos[1] / SQUARESIZE))
                print(checkerSelected)
            # select destination square with right mouse
            elif pg.mouse.get_pressed()[2] == True:
                mouse_pos = pg.mouse.get_pos()
                dest = (int(mouse_pos[0] / SQUARESIZE), int(mouse_pos[1] / SQUARESIZE))
                print(dest)

    # Player's move
    if checkerSelected is not None and board.isChecker(checkerSelected) and dest is not None:
        board.getChecker(checkerSelected).move(dest)
        checkerSelected = None
        dest = None

    # Drawing
    screen.blit(background_image, [0, 0])
    board.draw(screen)
    pg.display.flip()
