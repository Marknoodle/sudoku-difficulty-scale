#   Structure of a skill:
#   Part 1: Find where the skill can be applied (problem recognition)
#   Part 2: Apply skill
import math

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
    flipped_board = math.transpose(board)
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
    temp = math.transpose(board)
    return temp[cell[1]]

def subgroups_of_two(target):
    return [target[i: j] for i in range(len(target))
                         for j in range(i + 1, len(target) + 1) if len(target[i: j]) == 2]

def find_naked_pair(board, cell):
    row = cell[0]
    col = cell[1]
    target = board[row][col]
    
    for block, block_num in enumerate(board[row]):
        if block == target and block_num != col:
            return True
    for block, block_num in enumerate(ret_column(board, cell)):
        if block == target and block_num != row:
            return True
    for block, block_num in enumerate(ret_subgrid(board, cell)):
        if block == target and block_num != (3 * (math.floor(row/3)) + (math.floor(col/3))):
            return True
    return False

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
    
                    
            

def hidden_single(board, cell):
    '''
    description:    While there are technically multiple valid options
                    there is only one viable solution due to factors
                    that eliminate values in its subgrid/row/column
    input: 
    operations:

    output: True if success, False if failed
    '''
    None

def naked_single():
    '''
    description:
    input:
    operations:
    output: True if success, False if failed
    '''
    None

def naked_pair():
    '''
    description:
    input:
    operations:
    output: True if success, False if failed
    '''
    None

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