def human_years_cat_years_dog_years(y):
    if y == 1:
        return [1, 15, 15]
    elif y == 2:
        return [2, 24, 24]
    else:
        return [y, 24 + (y - 2) * 4, 24 + (y - 2) * 5]
