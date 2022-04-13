import board
import player
import skills

class Game:
    # active board:
    # answer board:
    # player: 
    def __init__(self, player, answer_board, active_board):
        self.player = player
        self.answer_board = answer_board
        self.active_board = active_board
    
    def check_win(self):
        if self.answer_board == self.active_board:
            print("You win!!")
            return True
    
    def perform_move(self, skill):
        move = self.player.skills[skill]
        

    
