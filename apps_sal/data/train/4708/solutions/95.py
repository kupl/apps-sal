def human_years_cat_years_dog_years(human_years):
    cat_years = 15 * (human_years >= 1) + 9 * (human_years >= 2) + 4 * max(human_years - 2, 0)
    return [human_years, cat_years, cat_years + max(human_years - 2, 0)]
