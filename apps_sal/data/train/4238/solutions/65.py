def squares_needed(grains):
    mysum = 0
    sq = 0
    while mysum < grains:
        mysum += 2**sq
        sq += 1
    return sq
