def human_years_cat_years_dog_years(human_years):

    if human_years >= 2:

        catYears = 15 + 9 + (human_years - 2) * 4
        dogYears = 15 + 9 + (human_years - 2) * 5

        return [human_years, catYears, dogYears]
    else:
        return [human_years, 15, 15]
