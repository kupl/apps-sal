def squares_needed(grains):
    g = 0
    count = 0
    for i in range(0,65):
        if g<grains:
            g = g+2**i
            count += 1
        else:
            return count
