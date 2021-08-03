def get_candy_position(n, r, c, candy):
    if candy > n:
        return [-1, -1, -1]

    linIdx = r * c - ((candy - 1) % (r * c) + 1)
    return [(candy - 1) // (r * c) + 1, linIdx // c, linIdx % c]
