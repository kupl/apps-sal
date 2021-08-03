def squares_needed(grains):
    count = 0
    i = 0
    while count < grains:
        count += 2**i
        i += 1
    return i
