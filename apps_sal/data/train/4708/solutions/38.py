def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        (cat_years, dog_years) = (15, 15)
    elif human_years == 2:
        (cat_years, dog_years) = (24, 24)
    else:
        cat_years = 24 + (human_years - 2) * 4
        dog_years = 24 + (human_years - 2) * 5
    return [human_years, cat_years, dog_years]
