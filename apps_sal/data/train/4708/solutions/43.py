def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        dog_years = 15
        cat_years = 15
    if human_years == 2:
        dog_years = 24
        cat_years = 24
    if human_years > 2:
        dog_years = 24 + ((human_years - 2) * 5)
        cat_years = 24 + ((human_years - 2) * 4)
    return [human_years, cat_years, dog_years]
