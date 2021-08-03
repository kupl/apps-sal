def count_red_beads(n):
    if n < 2:
        return 0
    if n > 2:
        red = (n - 1) * 2
        return red
