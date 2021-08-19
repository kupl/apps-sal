def human_years_cat_years_dog_years(human_years):
    catYears = 15
    DogYears = 15
    if human_years == 1:
        return [human_years, catYears, DogYears]
    elif human_years == 2:
        return [human_years, catYears + 9, DogYears + 9]
    elif human_years >= 3:
        n = human_years - 3
        s = 24 + n * 4 + 4
        f = 24 + n * 5 + 5
        return [human_years, s, f]
