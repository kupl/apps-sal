def get_candy_position(n, r, c, candy):
    if candy > n:
        return [-1, -1, -1]
    (box, res) = divmod(candy, r * c)
    if res == 0:
        return [box, 0, 0]
    (row, res) = divmod(res, c)
    return [box + 1, r - row, 0] if res == 0 else [box + 1, r - row - 1, c - res]
