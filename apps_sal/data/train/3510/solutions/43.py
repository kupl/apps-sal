def count_red_beads(n):
    counter = 0
    if n < 2:
        return counter
    else:
        for x in range(1, n):
            counter +=2
        return counter
