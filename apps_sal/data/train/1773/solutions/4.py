# Accessors
def get_row(board, row_index):
    return board[row_index]


def get_col(board, col_index):
    return [row[col_index] for row in board]


def get_subgrid(board, base_x, base_y):
    # Returns elements (array) in a 3x3 subgrid
    # base_x,base_y are the x,y coordinates of the top-left element in the 3x3 subgrid
    result = []
    for x in range(0, 3):
        for y in range(0, 3):
            result.append(board[base_x + x][base_y + y])
    return result


class InvalidSudokuSet(Exception):
    pass


def validate_9(arr, identifier="Group"):
    # Validates any 9 elements
    if len(arr) != 9:
        raise InvalidSudokuSet("{} has length {} (not 9): {}".format(identifier, len(arr), arr))

    for number in range(1, 10):
        if number not in arr:
            raise InvalidSudokuSet("{} is missing '{}': {}".format(identifier, number, arr))


def validate_dimensions(board):
    if len(board) != 9:
        raise InvalidSudokuSet("Board contains {} rows:\n{}".format(len(board), board))
    for row in board:
        if len(row) != 9:
            raise InvalidSudokuSet("Row does not have 9 columns:\n{}".format(board))


def validate_rows(board):
    for index in range(0, 9):
        validate_9(get_row(board, index), "Row")


def validate_columns(board):
    for index in range(0, 9):
        validate_9(get_col(board, index), "Column")


def validate_subgrids(board):
    for x in range(0, 3):
        for y in range(0, 3):
            subgrid = get_subgrid(board, x * 3, y * 3)
            validate_9(subgrid, identifier="3x3 Subgrid")


def validSolution(board):
    try:
        validate_dimensions(board)
        validate_rows(board)
        validate_columns(board)
        validate_subgrids(board)

    except InvalidSudokuSet as e:
        print("Invalid board:\n{}\n".format(board))
        print(e)
        return False

    print("Valid board:\n{}".format(board))
    return True
