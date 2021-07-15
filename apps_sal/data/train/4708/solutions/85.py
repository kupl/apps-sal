def human_years_cat_years_dog_years(human_years):
    return [human_years, 15, 15] if human_years <= 1 else \
        [human_years, 24, 24] if human_years <= 2 else \
        [human_years, 24+(human_years-2)*4, 24+(human_years-2)*5]
