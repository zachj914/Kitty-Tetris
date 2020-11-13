import time
import numpy as np

from graphics import *

BLOCK_SIZE = 22
FRAME_EDGE_LEFT=5
FRAME_EDGE_TOP=5

board = np.zeros((20, 10), dtype=np.int8)

#         [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,],
#          [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]]

class Piece:
    def __init__(self, ID, pic, shape=0, color=0):
        self.ID = ID
        self.color = color
        load_picture(pic, ID)
        if shape:
            for row in shape:
                for index, item in enumerate(row):
                    if item:
                        row[index] = ID
        self.shape = shape

    def draw(self, x=0, y=0):
        draw_piece(self.ID, x, y)
        
    def draw_grid(self, x=0, y=0):
        self.draw(FRAME_EDGE_LEFT + BLOCK_SIZE * x,
                  FRAME_EDGE_TOP + BLOCK_SIZE * y)

    def delete(self):
        delete_piece(self.ID)

    def drop(self):
        x = (len(board[1]) // 2) - ((len(self.shape[0])) // 2)
        y = 0
        while (y < len(board) - 1):
            self.draw_grid(x, y)
            refresh()
            self.delete()
            time.sleep(.5)
            y += 1
