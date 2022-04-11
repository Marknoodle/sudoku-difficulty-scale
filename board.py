import random
import numpy
import math
class Board:
    # style         -> the kind of game to be played, default is "standard" which is 9x9
    # block_size    -> the size of each subgrid, used to generate the board
    # board         -> a 2d list of ints which represent our board
    #                  to navigate: self.board[1,3] is the first row, third column
    # subgrids      -> a list of pairs, where the first element is the initial index
    #                  of a subgrid, and the second is the final. i.e.
    #                  ((1,3),(1,3)) is the upper left subgrid, ((7,9),(7,9)) is the bottom right 
    def __init__(self, board=None, block_size=3):
        self.block_size = block_size
        if board == None:
            self.board = [[0] * 3 * self.block_size ] * 3 * self.block_size
        else:
            self.board = board
        self.subgrid_starts = set([math.ceil(x/self.block_size) for x in range (len(self.board))])
        self.subgrid_rowcoords = [list(range(x,x+3)) for x in self.subgrid_starts]
        
    numpy.warnings.filterwarnings('ignore', category=numpy.VisibleDeprecationWarning)
    def check(self):
        for row in self.board:
            if len(row) > len(set(row)):
                return False
        for row in numpy.transpose(self.board):
            if len(row) > len(set(row)):
                return False
        
        subgrids = []
        for rows in self.subgrid_rowcoords:
            for cols in self.subgrid_rowcoords:
                subgrids.append([self.board[row][col] for row in rows for col in cols])
        for row in subgrids:
            if len(row) > len(set(row)):
                return False
        return True
                





    

