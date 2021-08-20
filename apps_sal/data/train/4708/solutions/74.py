def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        (catYears, dogYears) = (15, 15)
    elif human_years == 2:
        (catYears, dogYears) = (24, 24)
    else:
        catYears = 24 + (human_years - 2) * 4
        dogYears = 24 + (human_years - 2) * 5
    return [human_years, catYears, dogYears]
