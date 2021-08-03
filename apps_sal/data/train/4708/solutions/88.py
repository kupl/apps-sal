def human_years_cat_years_dog_years(human_years):
    f = 15
    s = 9
    if human_years == 1:
        return [human_years, f, f]
    elif human_years == 2:
        return [human_years, f + s, f + s]
    else:
        return [human_years, f + s + (human_years - 2) * 4, f + s + (human_years - 2) * 5]
