def human_years_cat_years_dog_years(human_years):
    if human_years >= 1:
        cat_years = 15
        dog_years = 15
    if human_years >= 2:
        cat_years += 9
        dog_years += 9
        for i in range(human_years - 2):
            cat_years += 4
            dog_years += 5
    return [human_years, cat_years, dog_years]
