def count_red_beads(n):
    r = 2
    if n < 2:
        return 0
    for x in range(2, n):
        r += 2
    return r
