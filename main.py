import sys
import os
import time
import curses

from graphics import *
from tetris import *

screen = curses.initscr()
curses.curs_set(False)

Frame = Piece(1, "Frame.png")
T = Piece(2, "T.png", [[1, 1, 1],
                       [0, 1, 0]], 0)
Frame.draw()
refresh()

T.drop()

curses.endwin()
clear_screen()
