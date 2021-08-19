def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        catYears = 15
        dogYears = 15
    elif human_years == 2:
        catYears = 24
        dogYears = 24
    elif human_years > 2:
        catYears = 24 + (human_years - 2) * 4
        dogYears = 24 + (human_years - 2) * 5
    years = []
    years.append(human_years)
    years.append(catYears)
    years.append(dogYears)
    return years
