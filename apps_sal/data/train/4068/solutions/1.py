def get_candy_position(n, r, c, candy):
    if candy > n:
        return [-1, -1, -1]
    label = (candy + r * c - 1) // (r * c)
    candy = (candy - 1) % (r * c)
    row = r - 1 - candy // c
    col = c - 1 - candy % c
    return [label, row, col]
