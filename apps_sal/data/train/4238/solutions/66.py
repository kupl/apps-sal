def squares_needed(grains):
    t = 0
    while grains > 0:
        t += 1
        grains = grains // 2
    return t
