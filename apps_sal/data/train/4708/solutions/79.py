def human_years_cat_years_dog_years(h):
    if h is 1:
        c = 15
        d = 15
    elif h is 2:
        c = 24
        d = 24
    else:
        c = 24 + (h - 2) * 4
        d = 24 + (h - 2) * 5
    return [h, c, d]
