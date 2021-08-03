def human_years_cat_years_dog_years(human_years):
    cat_years = 0
    dog_years = 0
    human = human_years
    if human >= 1:
        cat_years = 15
        dog_years = 15
        human = human - 1
    if human >= 1:
        cat_years += 9
        dog_years += 9
        human = human - 1
    if human >= 1:
        cat_years += human * 4
        dog_years += human * 5
    return [human_years, cat_years, dog_years]
