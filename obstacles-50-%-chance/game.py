from player import HumanPlayer, RandomComputerPlayer
import time
import random

# see README for more info on rules and logic


class TicTacToe:
    def __init__(self):

        self.board = [' ' for _ in range(16)]

        self.current_winner = None

    # prints empty board
    def print_board(self):
        # split up the rows
        for row in [self.board[i*4:(i+1)*4] for i in range(4)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        number_board = [[str(i).rjust(2) for i in range(j*4, (j+1)*4)]
                        for j in range(4)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')

    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

    def empty_squares(self):

        return ' ' in self.board

    def number_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):

        if self.board[square] == ' ':
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False

    def add_obstacle(self):
        if self.available_moves():
            obstacle_square = random.choice(self.available_moves())
            self.board[obstacle_square] = '*'

    def winner(self, square, letter):

        row_index = square // 4
        row = self.board[row_index*4: (row_index + 1) * 4]
        if all([spot == letter for spot in row]):
            return True

        column_index = square % 4
        column = [self.board[column_index+i*4] for i in range(4)]
        if all([spot == letter for spot in column]):
            return True

        # top left to bottom right diagonal
        if square in {0, 5, 10, 15}:
            diagonal1 = [self.board[i] for i in [0, 5, 10, 15]]
            if all(spot == letter for spot in diagonal1):
                return True

        # top right to bottom left diagonal
        if square in {3, 6, 9, 12}:
            diagonal2 = [self.board[i] for i in [3, 6, 9, 12]]
            if all(spot == letter for spot in diagonal2):
                return True

        return False


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_numbers()

    letter = 'X'

    while game.empty_squares():

        if letter == 'O':
            square = o_player.get_move(game)
        else:
            square = x_player.get_move(game)

        if game.make_move(square, letter):

            if print_game:
                print(letter + f' makes move to square {square}.')
                game.print_board()
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' has won!\n')
                return letter

            # randomly add obstacle 50% chance
            if random.random() < 0.5:
                game.add_obstacle()
                if print_game:
                    print("An obstacle has been added to the board.")
                    game.print_board()
                    print('')

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(1)

    if print_game:
        print('It\'s a tie.')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    tictactoe = TicTacToe()
    play(tictactoe, x_player, o_player, print_game=True)
