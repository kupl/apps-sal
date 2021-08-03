def human_years_cat_years_dog_years(human_years):
    cat_years = (lambda y: 15 + 9 * (0, 1)[y - 1 > 0] + 4 * (y - 2) * (0, 1)[y - 2 > 0])(human_years)
    dog_years = (lambda y: 15 + 9 * (0, 1)[y - 1 > 0] + 5 * (y - 2) * (0, 1)[y - 2 > 0])(human_years)
    return [human_years, cat_years, dog_years]
