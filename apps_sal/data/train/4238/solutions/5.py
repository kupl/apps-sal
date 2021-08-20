def squares_needed(grains):
    return next((i for i in range(99) if 1 << i > grains))
