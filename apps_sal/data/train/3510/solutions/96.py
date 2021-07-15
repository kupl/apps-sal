def count_red_beads(n):
    if n == 2:
        return n
    elif n > 2:
        return n * 2 - 2
    else:
        return 0
