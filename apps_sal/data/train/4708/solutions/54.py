def human_years_cat_years_dog_years(human_years):
    dog_years = 15 + min((human_years - 1), 1) * 9 + max((human_years - 2), 0) * 5
    cat_years = 15 + min((human_years - 1), 1) * 9 + max((human_years - 2), 0) * 4
    return [human_years, cat_years, dog_years]
