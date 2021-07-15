def human_years_cat_years_dog_years(human_years):
    catYears = dogYears = 0
    if human_years == 1:
        catYears = dogYears = 15
    elif human_years == 2:
        catYears = dogYears = 24
    else:
        catYears = 24 + (4 * (human_years - 2))
        dogYears = 24 + (5 * (human_years - 2))
    return [human_years, catYears, dogYears]
