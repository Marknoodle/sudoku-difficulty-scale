#   Structure of a skill:
#   Part 1: Find where the skill can be applied (problem recognition)
#   Part 2: Apply skill
import math
import numpy as np
import search

class Skills:
    def available_nums(board, cell):
        '''
        Returns the intersection of the valid values given by the row, column, and subgrid
        '''
        return list(set(search_row(board,cell)) & set(search_col(board, cell)) & set(search_subgrid(board, cell)))

    def search_row(board, cell):
        '''
        Returns the viable values given other known values in the row
        '''
        viable_vals = [1,2,3,4,5,6,7,8,9]
        row_num = cell[0]
        for block in board[row_num]:
            if block in viable_vals:
                viable_vals.remove(block)
        return viable_vals

    def search_col(board, cell):
        '''
        Returns the viable values given other known values in the column
        '''
        flipped_board = np.transpose(board)
        return search_row(flipped_board, cell)

    def search_subgrid(board, cell):
        '''
        Returns the viable values given other known values in the subgrid
        '''
        viable_vals = [1,2,3,4,5,6,7,8,9]
        for block in ret_subgrid(board,cell):
            if block in viable_vals:
                viable_vals.remove(block)
        return viable_vals

    def possible_vals(board):
        '''
        Returns a bord where each cell has a list of the possible values in said spot
        '''
        possible_board = [[],[],[],[],[],[],[],[],[]]
        for row,row_num in enumerate(board):
            for col,col_num in enumerate(board):
                possible_board[row_num][col_num] = available_nums(row_num,col_num)
        return possible_board

    def ret_subgrid(board, cell):
        row = cell[0]
        col = cell[1]
        return board.subgrids[3 * (math.floor(row/3)) + (math.floor(col/3))]

    def ret_column(board, cell):
        temp = flip_board(board)
        return temp[cell[1]]

    def flip_board(board):
        return np.transpose(board)

    def subgroups_of_two(target):
        return [target[i: j].sort() for i in range(len(target))
                            for j in range(i + 1, len(target) + 1) if len(target[i: j]) == 2]

    def find_hidden_single(board, cell):
        row = cell[0]
        col = cell[1]
        new_viable = board[row][col]

        for viable_vals in board[cell[0]][cell[1]]:
            for val in viable_vals:
                if search.num_appears_in_row(board, cell, val) == 1:
                    return [val]
                elif search.num_appears_in_col(board, cell, val) == 1:
                    return [val]
                elif search.num_appears_in_subgrid(board, cell, val) == 1:
                    return [val]
        return new_viable
            

    def find_naked_single(board, cell):
        row = cell[0]
        col = cell[1]
        
        if len(board[row][col]) == 1:
            return True
        else:
            return False

    def find_naked_pair(board, cell):
        row = cell[0]
        col = cell[1]
        target = board[row][col]
        
        if len(target) == 2:
            col_matches = search.full_matches_in_col(board, cell, target)
            row_matches = search.full_matches_in_row(board, cell, target)
            subgrid_matches = search.full_matches_in_subgrid(board, cell, target)
            if  row_matches[0] == 2:
                for viable_vals, index in enumerate(board[row]):
                    if set(target).issubset(set(viable_vals)) and (row, index) != (row, col) and (row, index) != row_matches[1]:
                        board[row][index].remove(target[0])
                        board[row][index].remove(target[1])
            if  col_matches[0] == 2:
                flipped_board = flip_board(board)
                for viable_vals, index in enumerate(flipped_board[col]):
                    if set(target).issubset(set(viable_vals)) and (index, col) != (row, col) and (index, col) != col_matches[1]:
                        board[index][col].remove(target[0])
                        board[index][col].remove(target[1])
            if  subgrid_matches[0] == 2:
                subgrid_num = cell_to_subgrid(cell)
                for viable_vals, subgrid_index in enumerate(board.subgrid[subgrid_num]):
                    new_cell = subgrid_to_cell(subgrid_num, subgrid_index)
                    new_row = new_cell[0]
                    new_col = new_cell[1]
                    if set(target).issubset(set(viable_vals)) and  new_cell != (row, col) and new_cell != subgrid_matches[1]:
                        board[new_row][new_col].remove(target[0])
                        board[new_row][new_col].remove(target[1])


    def find_hidden_pair(board, cell):
        row = cell[0]
        col = cell[1]
        target = board[row][col]
        if len(target) >= 2:
            possible_pairs = subgroups_of_two(target)
            for block, block_num in enumerate(board[row]):
                if len(block) > 1:
                    block_pairs = subgroups_of_two(block)
                    for block_pair in block_pairs:
                        for possible_pair in possible_pairs:
                            if block_pair == possible_pair and block_num != col:
                                return True
            for block, block_num in enumerate(ret_column(board,cell))
                if len(block) > 1:
                    block_pairs = subgroups_of_two(block)
                    for block_pair in block_pairs:
                        for possible_pair in possible_pairs:
                            if block_pair == possible_pair and block_num != row:
                                return True
            for block, block_num in enumerate(ret_subgrid(board, cell))
                if len(block) > 1:
                    block_pairs = subgroups_of_two(block)
                    for block_pair in block_pairs:
                        for possible_pair in possible_pairs:
                            if block_pair == possible_pair and block_num != block_num != (3 * (math.floor(row/3)) + (math.floor(col/3))):
                                return True
        return False
        

    def find_x_wing(board):
        x_wings = find_horizontal_x_wing(board)
        x_wings = x_wings + find_horizontal_x_wing(search.invert_board(board))
        return board

    def find_horizontal_x_wing(board):
        x_wings = []
        for row, row_num in enumerate(board):
            for viable_vals, col_num in enumerate(row):
                for target in viable_vals:
                    appears = search.num_appears_in_row(board, (row_num,col_num), target)
                    if appears == 2:
                        for nested_row in [0,1,2,3,4,5,6,7,8].remove(row_num):
                            appears2 = search.num_appears_in_row(board, (nested_row, col_num))
                            if target == board[nested_row][col_num] and appears2 == 2:
                                x_wings.append((row_num, nested_row, target))
        return x_wings

                

    def hidden_single(board, cell):
        '''
        description:    While there are technically multiple valid options
                        there is only one viable solution due to factors
                        that eliminate values in its subgrid/row/column
        input: 
        operations:

        output: True if success, False if failed
        '''
        row = cell[0]
        col = cell[1]
        board[row][col] = find_hidden_single(board, cell)

    def naked_single():
        # do nothing, we treat the singleton list as done

    def naked_pair(board, cell):
        find_naked_pair(board, cell)
        

    def hidden_pair():
        '''
        description:
        input:
        operations:
        output: True if success, False if failed
        '''
        None

    def x_wing():
        '''
        description: (explain the theory)
        input: four corners
        operations:
            Count steps
            apply the operation (extend this)
        output: True if success, False if failed
        '''
        None

    def swordfish():
        '''
        description:
        input:
        operations:
        output: True if success, False if failed
        '''
        None