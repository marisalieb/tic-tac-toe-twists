from player import HumanPlayer, RandomComputerPlayer
import time

# see README for more info on rules and logic


class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_winner = None

    def print_board(self):
        # split up the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')

    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + ' |')

    def available_moves(self):
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def number_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        # if valid move, then make move (assign square to letter), then return true, if invalid return false
        if self.board[square] == ' ':
            self.board[square] = letter

            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False

    def winner(self, square, letter):

        row_index = square // 3  # which row it is at
        row = self.board[row_index*3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True

        column_index = square % 3  # divide by three and then take the leftover
        column = [self.board[column_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        # check diagonals, so works only if the square is an even number
        if square % 2 == 0:

            # top left to bottom right diagonal
            diagonal1 = [self.board[i] for i in [0, 4, 8]]
            if all([spot == letter for spot in diagonal1]):
                return True

            # top right to bottom left diagonal
            diagonal2 = [self.board[i] for i in [2, 4, 6]]
            if all([spot == letter for spot in diagonal2]):
                return True

        # if all checks fail there is no winner yet
        return False


def play(game, x_player, o_player, print_game=True):

    if print_game:
        game.print_board_numbers()

    letter = 'X'  # starting letter

    while game.empty_squares():

        if letter == 'O':
            square = o_player.get_move(game)  # ask o player to get move
        else:
            square = x_player.get_move(game)

        if square is None:
            print(f"Player {letter} lost their turn due to timeout.\n")
            # skip to the next players turn
            letter = 'O' if letter == 'X' else 'X'
            continue

        if game.make_move(square, letter):
            if print_game:
                print(letter + f' makes move to square {square}.')
                game.print_board()  # prints the updated board
                print('')

            if game.current_winner:
                if print_game:
                    print(letter + ' has won!')
                return letter

            letter = 'O' if letter == 'X' else 'X'

        time.sleep(1)

    if print_game:
        print('It\'s a tie.')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    tictactoe = TicTacToe()
    play(tictactoe, x_player, o_player, print_game=True)
