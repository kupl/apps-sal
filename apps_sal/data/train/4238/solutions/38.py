def squares_needed(grains):
    curr, sq = 1, 0
    while grains > 0:
        grains -= curr
        curr *= 2
        sq += 1
    return sq
