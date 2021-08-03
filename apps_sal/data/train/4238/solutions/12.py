def squares_needed(grains):

    if grains == 0:
        return 0
    c = 1
    while 1:
        for i in range(1, 65):
            if c > grains:
                return i - 1
            c = c + c
