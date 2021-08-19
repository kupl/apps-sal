def squares_needed(grains):

    from math import ceil, log
#    squares = 64
    print(grains)

    if grains == 0:
        return 0
    else:
        return ceil(log(grains + 1, 2))
