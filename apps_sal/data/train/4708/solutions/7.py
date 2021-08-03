def human_years_cat_years_dog_years(human_years):
    if human_years > 2:
        cat_years = ((human_years - 2) * 4) + 24
        dog_years = ((human_years - 2) * 5) + 24
    elif human_years == 2:
        cat_years = 24
        dog_years = 24
    else:
        cat_years = 15
        dog_years = 15
    return [human_years, cat_years, dog_years]
