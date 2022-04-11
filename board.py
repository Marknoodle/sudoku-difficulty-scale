import random
import numpy
import math
class Board:
    # block_size    -> the size of each subgrid, used to generate the board
    # board         -> a 2d list of ints which represent our board
    #                  to navigate: self.board[1,3] is the first row, third column
    # subgrids      -> a list that contains each subgrid represented as a list, i.e.
    #                  [1,2,3]
    #                  [4,5,6]  ->  [1,2,3,4,5,6,7,8,9]
    #                  [7,8,9]
    #                  This makes it easier to check for uniqueness within a subgrid
    def __init__(self, board=[[0] * 3 * self.block_size ] * 3 * self.block_size, block_size=3):
        self.block_size = block_size
        self.board = board
        self.subgrids = []

        for starting_row_val in range(block_size):
            for starting_col_val in range(block_size):
                self.subgrids.append([self.board[row][col] for row in range(starting_row_val * 3, starting_row_val * 3 + 3) 
                                                           for col in range(starting_col_val * 3, starting_col_val * 3 + 3)])

    # This disables a warning that we do not care about 
    numpy.warnings.filterwarnings('ignore', category=numpy.VisibleDeprecationWarning)
    
    # Checks the validity of the sudoku board:
    # 1: checks that each row in the board contains unique values
    # 2: checks that each collumn in the board contains unique values
    # 3: checks that each subgrid in the board contains unique values
    # 4: If all of the above are true: return true
    def check(self):
        for row in self.board:
            if len(row) > len(set(row)):
                return False
        for col in numpy.transpose(self.board):
            if len(col) > len(set(col)):
                return False
        for subgrid in self.subgrids:
            if len(subgrid) > len(set(subgrid)):
                return False
        return True
                





    

