def human_years_cat_years_dog_years(human_years):
    return [1, 15, 15] if human_years == 1 else [2, 24, 24] if human_years == 2 else [human_years, (human_years - 2) * 4 + 24, (human_years - 2) * 5 + 24]
