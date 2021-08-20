def human_years_cat_years_dog_years(human_years):
    return [human_years, 15 if human_years == 1 else 24 if human_years == 2 else 4 * (human_years - 2) + 24, 15 if human_years == 1 else 24 if human_years == 2 else 5 * (human_years - 2) + 24]
