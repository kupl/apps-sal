def from_pos(s): return (ord(s[0]) - 65, int(s[1]) - 1)


def to_pos(i, j): return f"{chr(i+65)}{j+1}"


def available_moves(position):
    if not (isinstance(position, str)
            and len(position) == 2
            and position[0] in "ABCDEFGH"
            and position[1] in "12345678"):
        return []

    (x, y), res = from_pos(position), []
    for k, l in ((0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)):
        i, j = y + k, x + l
        while 0 <= i < 8 and 0 <= j < 8:
            res.append(to_pos(j, i))
            i, j = i + k, j + l
    return sorted(res)
