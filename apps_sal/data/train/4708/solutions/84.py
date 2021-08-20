def human_years_cat_years_dog_years(y):
    c = d = 15
    if y > 1:
        c = d = 24
    if y > 2:
        (c, d) = (c + 4 * (y - 2), d + 5 * (y - 2))
    return [y, c, d]
