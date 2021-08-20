def count_red_beads(n):
    if n < 2:
        return 0
    elif n == 2:
        return 2
    else:
        return (n - 2) * 2 + 2
