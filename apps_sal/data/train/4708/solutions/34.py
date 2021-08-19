def human_years_cat_years_dog_years(human_years):
    catYears = 15
    if human_years == 2:
        catYears = 15 + 9
    if human_years >= 3:
        catYears = 24 + (human_years - 2) * 4
    dogYears = 15
    if human_years == 2:
        dogYears = 15 + 9
    if human_years >= 3:
        dogYears = 24 + (human_years - 2) * 5
    return [human_years, catYears, dogYears]
