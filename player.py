import skills
import board
class Player:
    # list of known skills
    def __init__(self, skills, initial, final):
        self.skills = skills
        self.guess_board = initial
        self.answer_board = final

    def list_skills():
        for skill in self.skills:
            print(skill)

    def run(self):
        self.guess_board = possible_vals(self.guess_board)
        for row, row_num in enumerate(self.guess_board):
            for col, col_num in enumerate(row):
                if False:
                    # check if the boards match?
                elif len(self.guess_board[row_num][col_num]) == 1:
                    self.guess_board = naked_single(self.guess_board, (row_num, col_num))
                elif False:
                    # check for naked pair
                elif False:
                    # Check for hidden single
                elif False:
                    # Check for hidden pair
                elif False:
                    # Check for x-wing
                elif False:
                    # Check for swordfish
        
        