def whose_turn(positions):
    positions = positions.split(";")
    on_white_squares = [is_white_square(pos) for pos in positions]

    # Player's knights on black-black or white-white => odd number of moves
    white_pieces_match = on_white_squares[0] == on_white_squares[1]
    black_pieces_match = on_white_squares[2] == on_white_squares[3]

    # Equal number of moves => white to move
    return white_pieces_match == black_pieces_match


def is_white_square(pos):
    x, y = ord(pos[0]) - 97, int(pos[1])
    return x % 2 == y % 2
