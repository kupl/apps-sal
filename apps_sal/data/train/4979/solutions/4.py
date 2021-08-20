import math


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)


Direction = {'←': lambda position: Position(position.x - 1, position.y), '↑': lambda position: Position(position.x, position.y - 1), '→': lambda position: Position(position.x + 1, position.y), '↓': lambda position: Position(position.x, position.y + 1), '↖': lambda position: Position(position.x - 1, position.y - 1), '↗': lambda position: Position(position.x + 1, position.y - 1), '↘': lambda position: Position(position.x + 1, position.y + 1), '↙': lambda position: Position(position.x - 1, position.y + 1)}
PIEP_PIPER = 'P'


class Rat:

    def __init__(self, position, move):
        self.position = position
        self.move = move

    def is_deaf(self, piper):
        current_distance = piper.distance(self.position)
        distance_after_one_step = piper.distance(self.move(self.position))
        return current_distance - distance_after_one_step < 0


def count_deaf_rats(town_square):
    rats = []
    piper = None
    for (y, line) in enumerate(town_square):
        for (x, cell) in enumerate(line):
            if cell in Direction:
                rats.append(Rat(Position(x, y), Direction[cell]))
            elif cell == PIEP_PIPER:
                piper = Position(x, y)
    return len([rat for rat in rats if rat.is_deaf(piper)])
