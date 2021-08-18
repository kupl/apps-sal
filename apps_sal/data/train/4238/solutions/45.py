def squares_needed(grains):
    if grains < 1:
        return 0
    grains = grains // 2
    print(grains)
    return 1 + squares_needed(grains)
