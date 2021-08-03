def pawn_move_tracker(moves):
    board_state = [
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        [".", ".", ".", ".", ".", ".", ".", "."],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        [".", ".", ".", ".", ".", ".", ".", "."]
    ]

    board = Board(board_state)
    next_board = board
    player = 'P'

    for move in moves:
        next_board = board.play(move, player)
        if(next_board == None):
            return move + ' is invalid'

        player = 'P' if player == 'p' else 'p'

    return board.get_state()


class Pawn:
    def __init__(self, cell, player):
        self.cell = cell
        self.moved = False
        self.player = player
        self.is_white = player == 'P'
        self.is_black = player == 'p'
        self.forward_direction = -1 if self.is_white else 1

    def moveTo(self, cell):
        self.moved = True
        self.cell.remove_pawn()
        cell.add_pawn(self)
        self.cell = cell
        return cell

    def belongsTo(self, player):
        return self.player == player

    # returns true if this pawn can move to the given cell in the context of a chess board
    def canMoveTo(self, cell, board):
        # can't move ahead if cell is occupied
        if cell.is_occupied():
            return False

        steps_away = cell.row - self.cell.row

        if steps_away == self.forward_direction * 1:
            return True

        if steps_away == self.forward_direction * 2:
            cell_ahead = board.cellAt(self.cell.row + self.forward_direction, self.cell.col)
            return not self.moved and not cell_ahead.is_occupied()

    def canCapture(self, cell):
        cell_has_enemy = cell.is_occupied() and cell.pawn.player != self.player
        cell_is_ahead = cell.row - self.cell.row == self.forward_direction
        cell_is_adjacent = abs(cell.col - self.cell.col)
        return cell_has_enemy and cell_is_ahead and cell_is_adjacent


class Cell:
    def __init__(self, row, col, occupant):
        self.row = row
        self.col = col
        self.occupant = occupant

        if(occupant != '.'):
            self.pawn = Pawn(self, occupant)
        else:
            self.pawn = None

    def is_occupied(self):
        return not self.pawn == None

    def add_pawn(self, pawn):
        self.pawn = pawn
        self.occupant = pawn.player

    def remove_pawn(self):
        self.pawn = None
        self.occupant = '.'


class Board:
    def __init__(self, board_array):
        self.board_state = []

        for i, row in enumerate(board_array):
            board_row = []
            for j, occupant in enumerate(row):
                board_row.append(Cell(i, j, occupant))

            self.board_state.append(board_row)

    # returns all pawns in a given column. At most 2 pawns per column.
    def pawnsInColumn(self, col):
        cells = [row[col] for row in self.board_state]
        return [cell.pawn for cell in cells if cell.is_occupied()]

    def cellAt(self, row, col):
        if(row < 0 or row > 7 or col < 0 or col > 7):
            return None
        return self.board_state[row][col]

    def play(self, move, player):
        if(len(move) == 2):
            return self.playMove(move, player)
        else:
            return self.playCapture(move, player)

    def playMove(self, move, player):
        row, col = toCoords(move)
        cell = self.cellAt(row, col)
        pawns = self.pawnsInColumn(col)

        for pawn in pawns:
            if pawn.belongsTo(player) and pawn.canMoveTo(cell, self):
                pawn.moveTo(cell)
                return self
        return None

    def playCapture(self, move, player):
        col = toCol(move[0])
        capture_row, capture_col = toCoords(move[2:])
        cell = self.cellAt(capture_row, capture_col)
        pawns = self.pawnsInColumn(col)

        for pawn in pawns:
            if pawn.belongsTo(player) and pawn.canCapture(cell):
                pawn.moveTo(cell)
                return self
        return None

    def get_state(self):
        return list([list([cell.occupant for cell in row]) for row in self.board_state])


def toCoords(move):
    col = toCol(move[0])
    row = 8 - int(move[1])
    return [row, col]


def toCol(move):
    return (ord(move) - 97)
