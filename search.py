import board
import math
import numpy as np

class Search:

    def invert_board(board):
        return np.transpose(board)

    def cell_to_subgrid(cell):
        row = cell[0]
        col = cell[0]
        return(3 * math.floor(row/3) + math.floor(col/3))

    def subgrid_to_cell(subgrid_num, position_in_subgrid):
        sub_row = math.floor(position_in_subgrid/3)
        sub_col = position_in_subgrid % 3
        row = math.floor(subgrid_num/3)*3 + sub_row
        col = math.floor(subgrid_num/3)*3 + sub_col
        return(row, col)

    def num_appears_in_row(board, cell, target):
        count = 0
        for viable_vals in board[cell[0]]:
            for val in viable_vals:
                if val == target:
                    count += 1
        return count
    
    def num_appears_in_col(board, cell, target):
        inverted_board = invert_board(board)
        return(num_appears_in_row(inverted_board, cell, target))
    

    def num_appears_in_subgrid(board, cell, target):
        count = 0
        for viable_vals in board.subgrids[cell_to_subgrid(cell)]:
            for val in viable_vals:
                if val == target:
                    count += 1
        return count

    def full_matches_in_row(board, cell, target):
        count = 1
        for viable_vals, pos in enumerate(board[cell[0]]):
            if viable_vals == target:
                count += 1
                pos = (cell[0], pos)
        return (count, pos)
    
    def full_matches_in_col(board,cell,target):
        inverted_board = invert_board(board)
        row = cell[0]
        col = cell[1]
        return(full_matches_in_row(inverted_board, (col, row), target))

    def full_matches_in_subgrid(board, cell, target):
        count = 1
        for viable_vals, pos_in_subgrid in board.subgrids[cell_to_subgrid(cell)]:
            if viable_vals == target:
                count += 1
                pos = subgrid_to_cell(cell_to_subgrid(cell), pos_in_subgrid)
        return (count, pos)
