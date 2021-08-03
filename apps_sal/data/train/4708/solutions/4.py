def human_years_cat_years_dog_years(human_years, dog_years=15, cat_years=15):
    if human_years == 1:
        pass
    elif human_years == 2:
        cat_years = dog_years = 24
    else:
        cat_years = 4 * human_years + 16
        dog_years = 5 * human_years + 14
    return [human_years, cat_years, dog_years]
