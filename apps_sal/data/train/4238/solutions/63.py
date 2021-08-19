def squares_needed(grains):
    if grains == 0:
        return 0
    elif grains == 1:
        return 1
    else:
        return 1 + squares_needed(grains // 2)
