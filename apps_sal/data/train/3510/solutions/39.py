def count_red_beads(n):
    return range(0, 10001, 2)[n - 1 if n > 0 else n]
