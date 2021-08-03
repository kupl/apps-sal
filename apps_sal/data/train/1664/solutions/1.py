from collections import namedtuple
from functools import reduce
import enum
import sys


class Outcomes:
    """Enapsulation of outcomes to which tracks results as named attributes
    and can return the array expected by the kata.
    """

    def __init__(self):
        """Initialize situational count members to 0.
        """

        self.checkmates = 0
        self.checks = 0
        self.stalemates = 0
        self.alives = 0

    def as_array(self):
        """Return the array ordered as expected by the kata definition.

        Returns:
            array -- integer array of counts of squares by chess condition.
        """

        return [self.checkmates, self.checks, self.stalemates, self.alives]


class GameSquareConditions:
    """Gameplay conditions of a square.
    """

    def __init__(self, is_threatened=False, is_occupied=False, is_inhibited=False):
        self.is_threatened = is_threatened
        self.is_occupied = is_occupied
        self.is_inhibited = is_inhibited

    @property
    def is_safe(self):
        """Property to return the inverse of is_threatened.
        """
        return not self.is_threatened


class GameSquareOutcome(enum.Enum):
    CHECKMATE = enum.auto()
    CHECK = enum.auto()
    STALEMATE = enum.auto()
    ALIVE = enum.auto()
    UNKNOWN = enum.auto()


@enum.unique
class MovementDirection(enum.Enum):
    """Enumeration of movement directions.
    """
    NORTH = (0, 1)
    NORTH_EAST = (1, 1)
    EAST = (1, 0)
    SOUTH_EAST = (1, -1)
    SOUTH = (0, -1)
    SOUTH_WEST = (-1, -1)
    WEST = (-1, 0)
    NORTH_WEST = (-1, 1)

    def __init__(self, x_offset, y_offset):
        self.x_offset = x_offset
        self.y_offset = y_offset

    @property
    def cartesian_offset(self):
        """Return an (x,y) tuple offset for the direction. This method assumes
        the cartesian grid lower left is 0,0 with positive x to the right and
        positive y up.
        """
        return (self.x_offset, self.y_offset)

    @property
    def reciprical(self):
        """Return the opposite direction.
        """
        if self == self.NORTH:
            return self.SOUTH
        elif self == self.NORTH_EAST:
            return self.SOUTH_WEST
        elif self == self.EAST:
            return self.WEST
        elif self == self.SOUTH_EAST:
            return self.NORTH_WEST
        elif self == self.SOUTH:
            return self.NORTH
        elif self == self.SOUTH_WEST:
            return self.NORTH_EAST
        elif self == self.WEST:
            return self.EAST
        elif self == self.NORTH_WEST:
            return self.SOUTH_EAST

        raise ValueError("Unknown direction to recipricate!")

    def move_from(self, x, y):
        """Apply the movement to the provided X, Y cartesian coordinates.

        Arguments:
            x {int} -- Starting X cartesian coordinate to move from.
            y {int} -- Starting Y cartesian coordinate to move from.

        Returns:
            Tuple (x,y) cartesian coordinates resulting from the move.
        """
        offset = self.cartesian_offset
        return (x + offset[0], y + offset[1])


class GameSquare:
    """Square on the gameboard.
    """

    def __init__(self):
        """Initialize the neighbors in all directions to None.
        """
        self.neighbors = {}
        self.condition = GameSquareConditions()
        self.outcome = GameSquareOutcome.UNKNOWN

    def has_neighbor(self, direction):
        """Check if there is a neighboring square in the given direction.

        Arguments:
            direction {MovementDirection} -- Direction to check.
        """
        return self.neighbor(direction) is not None

    def neighbor(self, direction):
        """Return the neighboring game square in the direction. If no neighbor
        has been set, None.

        Arguments:
            direction {MovementDirection} -- Direction to get neighbor in.

        Return:
            GameSquare or None.
        """
        return self.neighbors.get(direction, None)

    def set_neighbor(self, neighbor, direction):
        """Store the neighbor to the specified direction.

        Side effects:
        Neighbor status is also set in the reciprical direction of the
        provided neighbor. If the neighbor is already set on that
        direction, it is cleared.

        If the provided neighbor is 'self' a 

        Arguments:
            neighbor {GameSquare} -- Neighboring game square to connect.
            direction {MovementDirection} -- Direction to get neighbor in.
        """
        if neighbor is self:
            raise ValueError("Cannot set yourself as a neighbor!")

        existing_neighbor = self.neighbor(direction)
        if existing_neighbor is not None and existing_neighbor is not neighbor:
            raise ValueError("Another neighbor is already in that direction!")

        recip_direction = direction.reciprical
        existing_recip_neighbor = neighbor.neighbor(recip_direction)
        if existing_recip_neighbor is not None and existing_recip_neighbor is not self:
            raise ValueError("Input neighbor already has neighbor in opposite direction!")

        self.neighbors[direction] = neighbor
        neighbor.neighbors[recip_direction] = self

    def neighbor_conditions(self):
        """Return a list of all conditions for neighboring squares.
        """
        return [n.condition for n in list(self.neighbors.values())]

    def render(self, out_dest):
        """Simple grid rendering to the output stream.

        Arguments:
            out_dest -- Output stream to render to.
        """

        marker = " "
        if self.condition.is_threatened:
            marker = "v"
        elif self.condition.is_occupied:
            marker = "*"
        elif self.condition.is_inhibited:
            marker = "-"
        out_dest.write(marker)

    def render_outcome(self, out_dest):
        """Simple grid rendering of the outcome to the output stream.

        Arguments:
            out_dest -- Output stream to render to.
        """

        marker = "?"
        if self.outcome == GameSquareOutcome.CHECKMATE:
            marker = "!"
        elif self.outcome == GameSquareOutcome.CHECK:
            marker = ":"
        elif self.outcome == GameSquareOutcome.STALEMATE:
            marker = "o"
        elif self.outcome == GameSquareOutcome.ALIVE:
            marker = "."
        out_dest.write(marker)


class Gameboard:
    """Gameboard comprised of rows and columns of GameSquares.
    The origin of the gameboard is the "lower-left".
    """

    def __init__(self, num_rows, num_cols):
        """Initialize the gameboard with a num_rows x num_cols grid of 
        GameSquares.

        Arguments:
            num_rows {int} -- Number of rows on the gameboard
            num_cols {int} -- Number of columns on the gameboard
        """
        if num_rows < 1:
            fmt = "Gameboard initialized with number of rows < 1 ({})!"
            msg = fmt.format(num_rows)
            raise ValueError()

        if num_cols < 1:
            fmt = "Gameboard initialized with number of columns < 1 ({})!"
            msg = fmt.format(num_cols)
            raise ValueError(msg)

        self.num_rows = num_rows
        self.num_cols = num_cols

        self.board = {}
        for row in range(num_rows):
            for col in range(num_cols):
                key = (row, col)
                self.board[key] = GameSquare()

        for row in range(num_rows):
            for col in range(num_cols):
                current = self.square_at(row, col)
                for direction in MovementDirection:
                    try:
                        neighbor_x, neighbor_y = direction.move_from(row, col)
                        neighbor = self.square_at(neighbor_x, neighbor_y)
                        current.set_neighbor(neighbor, direction)
                    except KeyError:
                        pass

    def square_at(self, row, col):
        """Return the GameSquare at the specified row and column.

        If row or col are out of bounds, an KeyError is raised.

        Arguments:
            row {int} -- 0 based index of the row to return the square from.
            col {int} -- 0 based index of the column to return the square from.

        Return:
            GameSquare at the specified index.
        """
        key = (row, col)
        return self.board[key]

    def render(self, out_dest):
        """Simple grid rendering to the output stream. The board is rendered
        with the "top" row on "top".

        Arguments:
            out_dest -- Output stream to render to.
        """
        out_dest.write("\n\nGameboard\n")
        for y in range(self.num_cols - 1, -1, -1):
            for x in range(self.num_rows):
                out_dest.write("|")
                self.square_at(x, y).render(out_dest)
            out_dest.write("|\n")

    def render_outcome(self, out_dest):
        """Simple grid rendering to the output stream. The board is rendered
        with the "top" row on "top".

        Arguments:
            out_dest -- Output stream to render to.
        """
        out_dest.write("\n\nOutcomes\n")
        for y in range(self.num_cols - 1, -1, -1):
            for x in range(self.num_rows):
                out_dest.write("|")
                self.square_at(x, y).render_outcome(out_dest)
            out_dest.write("|\n")


class DestinationMover:
    """The DestinationMover attempts to move along a path to reach
    a GameSquare. Only the final destination is returned.
    """

    def __init__(self, *args):
        """Initialize the path to move to.

        Arguments:
            *args {MovementDirection} -- Path to move along.
        """
        self.movement_path = list(args)

    def append_path(self, *args):
        """Append the provided MovementDirections to the path.
        """

        self.movement_path = self.movement_path + list(args)

    def execute(self, origin):
        """Follow the stored movement path from the provided origin.

        Arguments:
            origin {GameSquare} -- Position on the gameboard to be move from.

        Return:
            List of 1 item where the move terminated, or an empty list if the
            movement path cannot be completed.
        """
        current_location = origin
        for move in self.movement_path:
            next_location = current_location.neighbor(move)
            if next_location == None:
                return []
            current_location = next_location
        return [current_location]

    def __str__(self):
        """Return a nice, printable representation of the DestinationMover.
        """
        path = "-".join(p.name for p in self.movement_path)
        return "DestinationMover: " + path


class VectorMover:
    """The VectorMover moves from an origin location in a constant direction
    and returns each GameSquare along the movement path. The mover stops a 
    GameSquare is occupied or there is no next neighbor in the direction.
    """

    def __init__(self, direction=None):
        self.direction = direction

    def execute(self, origin):
        """Follow the stored direction until there are no neighboring squares or
        if a square is occupied.

        Arguments:
            origin {GameSquare} -- Position on the gameboard to be move from.

        Return:
            List of squares moved along the path.
        """
        if self.direction is None:
            return []

        visited = []
        neighbor = origin.neighbor(self.direction)
        while neighbor is not None and not neighbor.condition.is_occupied:
            visited.append(neighbor)
            neighbor = neighbor.neighbor(self.direction)

        return visited

    def __str__(self):
        """Return a nice, printable representation of the VectorMover.
        """
        return "VectorMover: " + self.direction.name


class GamePiece:

    def __init__(self, inhibit_as_well_as_threaten=False):
        self.inhibit_as_well_as_threaten = inhibit_as_well_as_threaten
        self.location = None
        self.movers = []

    def place_on_board(self, gamesquare):
        """Set the piece on the specified gamesquare.

        Arguments:
            gamesquare {GameSquare} -- Location on the gameboard to place piece.
        """
        self.location = gamesquare
        self.location.condition.is_occupied = True

    def impart_force(self):
        """Update the game squares based on the force abilities of the
        piece.

        Arguments:
            location {GameSquare} -- Position on the gameboard of the piece.

        Returns a list of the updated game squares.
        """
        if self.location is None:
            return []

        result = []
        for mover in self.movers:
            result = result + mover.execute(self.location)

        for square in result:
            square.condition.is_threatened = True
            if self.inhibit_as_well_as_threaten:
                square.condition.is_inhibited = True

        return result

    def __str__(self):
        """Return a nice, printable representation of the GamePiece.
        """
        mover_content = "\n  ".join([str(x) for x in self.movers])
        r = "\n  ".join(['GamePiece', mover_content])
        return r


def create_knight_movers():
    """Create the DestinationMovers for the possible knight moves.

    Returns:
        [list(DesintationMover)] -- List of movers to execute knight moves.
    """

    knight_paths = []
    knight_paths.append((MovementDirection.NORTH,
                         MovementDirection.NORTH,
                         MovementDirection.WEST))

    knight_paths.append((MovementDirection.NORTH,
                         MovementDirection.NORTH,
                         MovementDirection.EAST))

    knight_paths.append((MovementDirection.NORTH,
                         MovementDirection.WEST,
                         MovementDirection.WEST))

    knight_paths.append((MovementDirection.NORTH,
                         MovementDirection.EAST,
                         MovementDirection.EAST))

    knight_paths.append((MovementDirection.SOUTH,
                         MovementDirection.SOUTH,
                         MovementDirection.WEST))

    knight_paths.append((MovementDirection.SOUTH,
                         MovementDirection.SOUTH,
                         MovementDirection.EAST))

    knight_paths.append((MovementDirection.SOUTH,
                         MovementDirection.WEST,
                         MovementDirection.WEST))

    knight_paths.append((MovementDirection.SOUTH,
                         MovementDirection.EAST,
                         MovementDirection.EAST))

    return [DestinationMover(*x) for x in knight_paths]


def create_rook_movers():
    """Create the VectorMovers for the possible rook moves.

    Returns:
        [list(VectorMover)] -- List of movers to execute rook moves.
    """
    directions = (MovementDirection.NORTH,
                  MovementDirection.SOUTH,
                  MovementDirection.EAST,
                  MovementDirection.WEST)
    return [VectorMover(direction) for direction in directions]


def create_bishop_movers():
    """Create the VectorMovers for the possible bishop moves.

    Returns:
        [list(VectorMover)] -- List of movers to execute bishop moves.
    """
    directions = (MovementDirection.NORTH_EAST,
                  MovementDirection.NORTH_WEST,
                  MovementDirection.SOUTH_EAST,
                  MovementDirection.SOUTH_WEST)
    return [VectorMover(direction) for direction in directions]


def create_amazon():
    piece = GamePiece()

    for mover in create_knight_movers():
        piece.movers.append(mover)

    for mover in create_rook_movers():
        piece.movers.append(mover)

    for mover in create_bishop_movers():
        piece.movers.append(mover)

    return piece


def create_king():
    piece = GamePiece(inhibit_as_well_as_threaten=True)
    for direction in MovementDirection:
        mover = DestinationMover()
        mover.append_path(direction)
        piece.movers.append(mover)

    return piece


def chess_location_to_game_indicies(pos_string):
    """Convert chess locations (ex A1) to index for a gameboard.

    Arguments:
            pos_string {string} -- Chess notation location on the board.

    Return:
        (x,y) tuple to index the gameboard.
    """
    first = ord(pos_string[0].upper()) - ord('A')
    second = int(pos_string[1]) - 1
    return (first, second)


def determine_square_status_and_update_outcome(my_condition,
                                               neighbor_conditions,
                                               outcome):
    """Determine the status of the square from the square's condition and
    the neighboring conditions. Update and return the outcome.

    Return the outcome type.

    Arguments:
        my_condition {GameSquareConditions} -- Condition of the square to evaluate
        neighbor_conditions {list(GameSquareConditions)} -- Conditions of nieghbors
        outcome {Outcomes} -- Cumulative outcome of the gameboard.
    """
    outcome_type = GameSquareOutcome.UNKNOWN
    if my_condition.is_occupied or my_condition.is_inhibited:
        return outcome_type

    can_move_to_safety = any([x.is_safe for x in neighbor_conditions])
    if my_condition.is_threatened:
        if can_move_to_safety:
            outcome.checks += 1
            outcome_type = GameSquareOutcome.CHECK
        else:
            outcome.checkmates += 1
            outcome_type = GameSquareOutcome.CHECKMATE

    else:
        if can_move_to_safety:
            outcome.alives += 1
            outcome_type = GameSquareOutcome.ALIVE
        else:
            outcome.stalemates += 1
            outcome_type = GameSquareOutcome.STALEMATE

    return outcome_type


def amazon_check_mate(king, amazon):

    outcomes = Outcomes()
    king_coords = chess_location_to_game_indicies(king)
    amazon_coords = chess_location_to_game_indicies(amazon)

    board = Gameboard(8, 8)
    king_piece = create_king()
    amazon_piece = create_amazon()

    king_piece.place_on_board(board.square_at(*king_coords))
    amazon_piece.place_on_board(board.square_at(*amazon_coords))

    king_piece.impart_force()
    amazon_piece.impart_force()

    for square in list(board.board.values()):
        determine_square_status_and_update_outcome(square.condition,
                                                   square.neighbor_conditions(),
                                                   outcomes)

    return outcomes.as_array()
