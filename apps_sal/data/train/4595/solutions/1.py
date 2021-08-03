# Convert chess notation to zero indexed tuple (x, y)
def int_pos(s): return (ord(s[0]) - ord("a"), int(s[1]) - 1)
# Convert zero indexed tuple (x, y) to chess notation
def note_pos(t): return "{}{}".format(chr(t[0] + ord("a")), t[1] + 1)


def bishop_extend(pos, move):
    """
    Extend a bishops attack position in the given move
    direction, until a legal move is not possible
    yielding each legal position in turn
    """
    x, y = pos
    dx, dy = move
    while 0 <= x + dx < 8 and 0 <= y + dy < 8:
        x += dx
        y += dy
        yield (x, y)


def bishop_attack(pos):
    """
    Given a position, return a dict of all possible 
    attackable positions and the direction of movement
    required to attack that position
    """
    result = {}
    for dx, dy in [(x, y) for x in [-1, 1] for y in [-1, 1]]:
        for attack_pos in bishop_extend(pos, (dx, dy)):
            result[attack_pos] = (dx, dy)
    return result


def bishop_diagonal(bishop1, bishop2):
    """
    Given two bishops on a chess board, if they are able to attack each other
    move them as far apart as possible.
    """
    b1, b2 = int_pos(bishop1), int_pos(bishop2)
    b1_attack, b2_attack = bishop_attack(b1), bishop_attack(b2)
    if b1 in b2_attack:
        # Attack paths intersect
        b1d, b2d = b1_attack[b2], b2_attack[b1]
        # move b1 in the direction b2 attacked and keep last legal move
        bishop1 = note_pos(list(bishop_extend(b1, b1d))[-1])
        # Same for b2
        bishop2 = note_pos(list(bishop_extend(b2, b2d))[-1])
    return sorted([bishop1, bishop2])
