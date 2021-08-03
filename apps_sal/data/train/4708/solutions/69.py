def human_years_cat_years_dog_years(human_years):
    cat_years = 15 * (human_years >= 1) + 9 * (human_years >= 2) + 4 * (human_years > 2) * (human_years - 2)
    dog_years = 15 * (human_years >= 1) + 9 * (human_years >= 2) + 5 * (human_years > 2) * (human_years - 2)
    return [human_years, cat_years, dog_years]
