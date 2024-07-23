import random

# see README for more info on rules and logic


class Player:
    def __init__(self, letter):
        self.letter = letter
        self.elements = ['E', 'W', 'F']
        self.element_counts = {'E': 0, 'W': 0, 'F': 0}

    def get_move(self, game):
        pass

    def choose_element(self):
        return random.choice(self.elements)

    def increment_element_count(self, elem):
        self.element_counts[elem] += 1


class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        square = random.choice(game.available_moves())

        element = self.choose_element()
        self.increment_element_count(element)

        return square, element


class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):

        valid_square = False
        value = None
        element = None

        while not valid_square:
            try:
                square = input('\n' + self.letter +
                               '\'s turn. Input move (0-8):')
                value = int(square)
                if value not in game.available_moves():
                    raise ValueError('Invalid square. Try again please.')

                elem = input(
                    f'Choose element (E for Earth, W for Wind, F for Fire): ').upper()
                if elem not in self.elements:
                    print('Invalid element. Choose E, W, or F.')

                if self.element_counts[elem] >= 3:
                    raise ValueError(
                        "You have already used this element 3 times.")

                valid_square = True
                element = elem

            except ValueError as e:
                print(e)
                print('Invalid input. Try again please.')

        self.increment_element_count(element)

        return value, element
