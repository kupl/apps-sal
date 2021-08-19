def count_red_beads(n):
    a = -2
    for i in range(n):
        a += 2
    return a if a > 0 else 0
