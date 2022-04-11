import random
from numpy import numpy.transpose
class Board:
    # style         -> the kind of game to be played, default is "standard" which is 9x9
    # block_size    -> the size of each subgrid, used to generate the board
    # board         -> a 2d list of ints which represent our board
    #                  to navigate: self.board[1,3] is the first row, third column
    # subgrids      -> a list of pairs, where the first element is the initial index
    #                  of a subgrid, and the second is the final. i.e.
    #                  ((1,3),(1,3)) is the upper left subgrid, ((7,9),(7,9)) is the bottom right 
    __init__(style='standard', board=None):
        self.style = style
        if style == 'standard':
            self.block_size = 3
        if board == None:
            self.board = [[0] * 3 * self.block_size ] * 3 * self.block_size
        else:
            self.board = board
        self.subgrids = []
        for x in range(1, (1 + self.block_size) * 3,3):
            for y in range(1, (1 + self.block_size) * 3,3):
                self.subgrids = self.subgrids + [((x, x + self.block_size),(y, y + self.block_size))]

    def board_check():
        for row in self.board:
            if len(row) > len(set(row)):
                return False
        for row in numpy.transpose(self.board):
            if len(row) > len(set(row)):
                return False
        subgrids = [[self.board[x:x+3][y:y+3] for x in range(1,(self.block_size * 3) + 1,3) for y in range(1,(self.block_size * 3) + 1,3)]]
        for row in subgrids:
            if len(row) > len(set(row)):
                return False
        return True
                





    

