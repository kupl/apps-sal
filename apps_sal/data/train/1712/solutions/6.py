from enum import Enum


class Positions(Enum):
    UPPER_LEFT = 1
    UPPER_RIGTHT = 2
    BOTTOM_LEFT = 3
    BOTTOM_RIGTHT = 4


class PuzzlePiece:
    def __init__(self, tup):
        self.values = {Positions.UPPER_LEFT: tup[0][0], Positions.UPPER_RIGTHT: tup[0][1],
                       Positions.BOTTOM_LEFT: tup[1][0], Positions.BOTTOM_RIGTHT: tup[1][1]}
        self.id = tup[2]
        self.corner = None
        values_lst = [value for position, value in list(self.values.items())]
        corners_positions_with_values = {Positions.UPPER_LEFT: Positions.BOTTOM_RIGTHT, Positions.UPPER_RIGTHT: Positions.BOTTOM_LEFT,
                                         Positions.BOTTOM_LEFT: Positions.UPPER_RIGTHT, Positions.BOTTOM_RIGTHT: Positions.UPPER_LEFT}
        if 3 == values_lst.count(None):
            for position in corners_positions_with_values:
                if self.values[position] is not None:
                    self.corner = corners_positions_with_values[position]


class Puzzle:
    def __init__(self, pieces):
        self.cornaners = dict()
        self.piece_map = dict()
        for piece in pieces:
            piece = PuzzlePiece(piece)
            if piece.corner is not None:
                self.cornaners[piece.corner] = piece
            for position, value in list(piece.values.items()):
                if value is not None:
                    if value not in self.piece_map:
                        self.piece_map[value] = {Positions.UPPER_LEFT: None, Positions.UPPER_RIGTHT: None,
                                                 Positions.BOTTOM_LEFT: None, Positions.BOTTOM_RIGTHT: None}
                    self.piece_map[value][position] = piece

    def solve(self):
        res = [[self.cornaners[Positions.UPPER_LEFT]]]
        while True:
            if res[-1][-1].values[Positions.BOTTOM_RIGTHT] is not None:
                res[-1].append(self.piece_map[res[-1][-1].values[Positions.BOTTOM_RIGTHT]][Positions.BOTTOM_LEFT])
            elif res[-1][0].values[Positions.BOTTOM_RIGTHT] is not None:
                res.append([])
                res[-1].append(self.piece_map[res[-2][0].values[Positions.BOTTOM_RIGTHT]][Positions.UPPER_RIGTHT])
            elif res[-1][-1].values[Positions.UPPER_RIGTHT] is not None:
                res[-1].append(self.piece_map[res[-1][-1].values[Positions.UPPER_RIGTHT]][Positions.UPPER_LEFT])
            else:
                break
        res = [tuple(piece.id for piece in row) for row in res]
        return res


def puzzle_solver(pieces, width, height):
    puzzle = Puzzle(pieces)
    return puzzle.solve()
