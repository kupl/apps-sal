def get_candy_position(n, r, c, candy):
    (q1, r1) = divmod(candy - 1, r * c)
    (q2, r2) = divmod(r1, c)
    return [-1, -1, -1] if n < candy else [q1 + 1, r - q2 - 1, c - r2 - 1]
