def squares_needed(grains, v=0, sum=0):
    if sum >= grains:
        return 0
    v = (v * 2) if v > 0 else (v + 1)
    return 1 + squares_needed(grains, v, sum + v)
