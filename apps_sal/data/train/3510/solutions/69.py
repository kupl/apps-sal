def count_red_beads(n):
    numOfRed = 0
    if n < 2:
        return 0
    else:
       numOfRed += n * 2 - 2
    return numOfRed
