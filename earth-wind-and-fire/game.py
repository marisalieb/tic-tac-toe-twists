from player import HumanPlayer, RandomComputerPlayer
import time

# see README for more info on rules and logic


class TicTacToe:
    def __init__(self):
        self.board = [(' ', ' ') for _ in range(9)]
        self.current_winner = None
        self.moves = {'X': {'E': 0, 'W': 0, 'F': 0},
                      'O': {'E': 0, 'W': 0, 'F': 0}}

    def print_board(self):
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join([f'{elem}{player}'.center(2)
                  for elem, player in row]) + ' |')

    @staticmethod
    def print_board_numbers():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + ' |')

    def available_moves(self):
        return [i for i, spot in enumerate(self.board) if spot == (' ', ' ')]

    def empty_squares(self):
        return (' ', ' ') in self.board

    def number_empty_squares(self):
        return self.board.count((' ', ' '))

    def make_move(self, square, letter, element):
        if self.board[square] == (' ', ' '):
            self.board[square] = element, letter
            self.moves[letter][element] += 1

            if self.winner(square):
                self.current_winner = self.winner(square)

            return True

        return False

    def check_winner_in_line(self, line):
        elements = [spot[0] for spot in line if spot != (' ', ' ')]
        player_letter = [spot[1] for spot in line if spot != (' ', ' ')]
        unique_elements = set(elements)

        for element in unique_elements:
            if elements.count(element) == len(line):
                x_count = player_letter.count('X')
                o_count = player_letter.count('O')
                if x_count > o_count:
                    return 'X'
                elif o_count > x_count:
                    return 'O'
        return None

    def winner(self, square):

        size = 3  # for 3x3; could also adjust for 4x4 board, but would need a bit more adjusting above
        lines_to_check = []

        # check rows
        row_index = square // size
        row = self.board[row_index * size: (row_index + 1) * size]
        lines_to_check.append(row)

        # check columns
        column_index = square % size
        column = [self.board[column_index + i * size] for i in range(size)]
        lines_to_check.append(column)

        # check diagonals
        if square % 2 == 0:
            diagonal1 = [self.board[i * (size + 1)] for i in range(size)]
            diagonal2 = [self.board[i * (size - 1) + (size - 1)]
                         for i in range(size)]
            lines_to_check.append(diagonal1)
            lines_to_check.append(diagonal2)

        for line in lines_to_check:
            winner = self.check_winner_in_line(line)
            if winner:
                self.current_winner = winner
                return True

        return False


def play(game, x_player, o_player, print_game=True):
    element_names = {'E': 'Earth', 'W': 'Wind', 'F': 'Fire'}

    if print_game:
        game.print_board_numbers()

    letter = 'X'  # starting letter

    while game.empty_squares():

        if letter == 'O':
            try:
                square, element = o_player.get_move(game)
            except ValueError as e:
                print(e)
                continue

        else:
            try:
                square, element = x_player.get_move(game)
            except ValueError as e:
                print(e)
                continue

        if game.make_move(square, letter, element):

            if print_game:
                element_full_name = element_names[element]
                print(
                    f'\n{letter} makes move to square {square} with {element_full_name}.')
                game.print_board()
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
