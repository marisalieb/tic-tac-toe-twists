import random
import time

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
        square = random.choice(game.available_moves())
        return square


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):

        valid_square = False
        value = None

        while not valid_square:

            start_time = time.time()

            square = input(self.letter + '\'s turn. Input move (0-8):')

            elapsed_time = time.time() - start_time
            if elapsed_time > 3:
                print(f'Player {self.letter} took too long!')
                return None

            try:
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError
                valid_square = True
            except ValueError:
                print('Invalid square. Try again please.')

        return value  # thats so human players next move
