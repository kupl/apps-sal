def human_years_cat_years_dog_years(human_years):
    return [human_years, 15 + (9 if human_years >= 2 else 0) + ((human_years - 2) * 4 if human_years >= 2 else 0), 15 + (9 if human_years >= 2 else 0) + ((human_years - 2) * 5 if human_years >= 2 else 0)]
