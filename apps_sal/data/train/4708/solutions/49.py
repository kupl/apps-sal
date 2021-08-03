def human_years_cat_years_dog_years(human_years):
    c = 15
    d = 15
    if human_years == 2:
        c = 15 + 9
        d = 15 + 9
    if human_years > 2:
        c = 24 + ((human_years - 2) * 4)
        d = 24 + ((human_years - 2) * 5)
    return [human_years, c, d]
