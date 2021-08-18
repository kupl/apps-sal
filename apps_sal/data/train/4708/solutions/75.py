def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat_y, dog_y = 15, 15
    elif human_years == 2:
        cat_y, dog_y = 24, 24
    else:
        cat_y = 24 + 4 * (human_years - 2)
        dog_y = 24 + 5 * (human_years - 2)
    return [human_years, cat_y, dog_y]
