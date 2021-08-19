def to_coords(s):
    return (ord(s[0]) - 96, int(s[1]))


def from_coords(i, j):
    return f'{chr(i + 96)}{j}'


L = ((1, 2), (1, -2), (-1, 2), (-1, -2), (2, 1), (2, -1), (-2, 1), (-2, -1))


def possible_positions(pos):
    (i, j) = to_coords(pos)
    return sorted((from_coords(i + k, j + l) for (k, l) in L if 0 < i + k <= 8 and 0 < j + l <= 8))
