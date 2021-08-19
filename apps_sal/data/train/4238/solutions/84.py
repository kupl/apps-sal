def squares_needed(grains):
    if grains <= 1:
        return grains
    grain_ammount = [grains]
    while grains >= 2:
        grain_ammount.append(grains / 2)
        grains = grains / 2
    return len(grain_ammount)
