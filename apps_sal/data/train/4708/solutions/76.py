def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        cat, dog = 15, 15
    if human_years == 2:
        cat, dog = 24, 24
    if human_years >= 3:
        cat = 24 + (human_years - 2) * 4
        dog = 24 + (human_years - 2) * 5
    return [human_years, cat, dog]
