import random
class Board:
    # style: the kind of game to be played, default is "standard" which is 9x9
    __init__(style='standard'):
        self.style = style
        if style == 'standard':
            self.block_size = 3 


    # We are going to establish the sudoku board as a dictionary
    # We will position the row/cols with {number}{letter}
    # To write to the top left square: board["1A"] = number
    # Remember that the keys are strings and the values stored are integers
    letters = [A,B,C,D,E,F,G,H,I]
    self.board = {}
    for i in range(1,10):
        for j in letters:
            board[f"{i}{j}"] = 0
    
    # subgrids -> the representation of each subgrid, numbered (1,2) for the 1st row, 2nd column
    # for      -> generates a dictionary storing the different grids which we can use to store 
    #               the remaining list elements
    # vals     -> the possible values to store in our subgrids, rows, and columns
    vals = [1,2,3,4,5,6,7,8,9]
    self.subgrids = []
    for i in range(1,4):
        for j in range(1,4):
            self.subgrids[f"{i}{j}"] = [vals]


    self.choices = {}
    for i in range(1,10):
        self.choices[f"{i}"] = vals
    for i in letters:
        self.choices[f"{i}"] = vals

    
    # Random puzzle maker -> (no rules just random start and pick numbers from there)
    def make():
        if  self.style == 'standard':
            global_choices = [1,2,3,4,5,6,7,8,9]
            local_choices = [1,2,3,4,5,6,7,8,9]
            for square in self.board:
                self.board[square] = random.choice(local)




    

