import random

# tic tac toe where wither the player can play against another player or against the computer
# see README for more info on rules and logic


class Player:
    def __init__(self, letter):
        self.letter = letter

    def get_move(self, game):
        pass


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        # get a random valid empty spot on the board
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):

        valid_square = False
        value = None  # user hasnt input a value yet

        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')

            try:  # if either of the following goes wrong its invalid input, if we pass both then valid square = true
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again please.')
        return value  # thats so human players next move
