from player import HumanPlayer, RandomComputerPlayer
import time

# see README for more info on rules and logic


class TicTacToe:
    def __init__(self):
        # for the board use a list by length of 9 which will represent the 3x3 board
        # assign an index in this length 9 list to each of the spaces and that will represent the board
        self.board = [' ' for _ in range(9)]

        self.current_winner = None

    # prints empty board
    def print_board(self):
        # split up the rows
        for row in [self.board[i*3:(i+1)*3] for i in range(3)]:
            print('| ' + ' |'.join(row) + ' |')

    @staticmethod  # prints basic explanatory board at top, tells you which number corresponds to which spot
    def print_board_numbers():
        number_board = [[str(i) for i in range(j*3, (j+1)*3)]
                        for j in range(3)]
        for row in number_board:
            print('| ' + ' |'.join(row) + ' |')

    def available_moves(self):  # to keep track but doesnt get printed
        return [i for (i, spot) in enumerate(self.board) if spot == ' ']
        # if spot is ' ' put i into list and then return entire list of indexes

    def empty_squares(self):
        # this will just become boolean and return boolean value if ' ' is there
        return ' ' in self.board

    def number_empty_squares(self):
        return self.board.count(' ')  # count number of ' ' in self.board

    # which square does the user want their move to be at and what letter the player is
    def make_move(self, square, letter):
        # if valid move, then make move (assign square to letter), then return true, if invalid return false
        if self.board[square] == ' ':  # so if its empty
            self.board[square] = letter  # then assign letter to that square

            # toggle current winner to the winner if there is one:
            # pass in the last move because if so that would be the winning move
            if self.winner(square, letter):
                self.current_winner = letter

            return True
        return False

    # winner if 3 in a row, column or diagonal
    def winner(self, square, letter):

        row_index = square // 3  # which row it is at
        row = self.board[row_index*3: (row_index + 1) * 3]
        if all([spot == letter for spot in row]):
            return True  # if all things in the row equal to that letter so all same letter

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


# print game set to true if human plays, if pc plays against py can set it to false
def play(game, x_player, o_player, print_game=True):

    # print the static method of the simple board
    if print_game:
        game.print_board_numbers()  # see which numbers correspond to which spot

    letter = 'X'  # starting letter

    # keep iterating while there are still empty squares

    while game.empty_squares():
        # get a move from the right player
        if letter == 'O':
            square = o_player.get_move(game)  # ask o player to get move
        else:
            square = x_player.get_move(game)

        # define function to make a move
        if game.make_move(square, letter):  # if this is valid
            if print_game:
                print(letter + f' makes move to square {square}.')
                game.print_board()  # prints the updated board
                print('')

            # so if current winner isnt set to None anymore, then that player won and end the game
            if game.current_winner:
                if print_game:
                    print(letter + ' has won!')
                return letter

            # after move made then alternate letters to switch players
            # assign letter to o if old letter was x otherwise assign to x
            letter = 'O' if letter == 'X' else 'X'

        # small break for computer to make a move, more organic that way
        time.sleep(1)

    if print_game:  # so when other loop is over
        print('It\'s a tie.')


if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = RandomComputerPlayer('O')
    tictactoe = TicTacToe()
    play(tictactoe, x_player, o_player, print_game=True)
