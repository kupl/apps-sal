tbl = str.maketrans('', '', 'aceg1357;')


def whose_turn(positions):
    return not len(positions.translate(tbl)) % 2
