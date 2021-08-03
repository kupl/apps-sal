from math import ceil


def get_candy_position(n, r, c, candy):
    if candy > n:
        return [-1, -1, -1]
    box = ceil(candy / (r * c))
    candy -= (box - 1) * r * c
    row = r - ceil(candy / c)
    column = c - candy % c if candy % c > 0 else 0
    return [box, row, column]
