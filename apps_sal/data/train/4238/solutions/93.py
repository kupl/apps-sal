def squares_needed(grains):
    count = 0
    print(grains)
    if grains == 0:
        return grains
    product = 1
    while grains >= 1:
        count += 1
        grains -= product
        product *= 2
    return count
