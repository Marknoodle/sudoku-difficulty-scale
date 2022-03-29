class Board:
    # style: the kind of game to be played, default is "standard" which is 9x9
    __init__(style='standard'):
        self.style = style


    # We are going to establish the sudoku board as a dictionary
    # We will position the row/cols with {number}{letter}
    # To write to the top left square: board["1A"] = number
    # Remember that the keys are strings and the values stored are integers
    letters = [A,B,C,D,E,F,G,H,I]
    board = {}
    for i in range(1,10):
        for j in letters:
            board[f"{i}{j}"] = -1
    


    

