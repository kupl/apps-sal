def human_years_cat_years_dog_years(human_years):
    return [human_years, 15 if human_years == 1 else 15 + 9 if human_years == 2 else 15 + 9 + (human_years - 2) * 4, 15 if human_years == 1 else 15 + 9 if human_years == 2 else 15 + 9 + (human_years - 2) * 5]
