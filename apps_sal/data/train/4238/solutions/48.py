def squares_needed(grains):
    if grains < 1:
        return 0
    total_wheat_rice = 0
    for i in range(64):
        total_wheat_rice += 2 ** i
        if total_wheat_rice >= grains:
            return i + 1
