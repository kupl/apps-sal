def squares_needed(grains, s=1, k=1):
    if grains == 0:
        return 0
    while s * 2 <= grains:
        s *= 2
        k += 1
    return k
