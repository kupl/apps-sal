def human_years_cat_years_dog_years(hy):
    if hy == 1:
        return [1, 15, 15]
    elif hy == 2:
        return [2, 24, 24]
    else:
        return [hy, 24 + 4 * (hy - 2), 24 + 5 * (hy - 2)]
    return [0, 0, 0]
