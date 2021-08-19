def human_years_cat_years_dog_years(human_years):
    print(human_years)
    (cat_years, dog_years) = (0, 0)
    if human_years == 1:
        cat_years = 15
        dog_years = 15
    if human_years == 2:
        cat_years = 24
        dog_years = 24
    if human_years >= 3:
        cat_years += 4 * (human_years - 2) + 24
        dog_years += 5 * (human_years - 2) + 24
    return [human_years, cat_years, dog_years]
