def human_years_cat_years_dog_years(human_years):
    return [human_years, 15 + 9 * (1 % human_years) + 4 * (human_years - 2) * (1 % human_years), 15 + 9 * (1 % human_years) + 5 * (human_years - 2) * (1 % human_years)]


def human_years_cat_years_dog_years2(human_years):
    return [human_years, 15 if human_years < 2 else 15 + 9 + 4 * (human_years - 2), 15 if human_years < 2 else 15 + 9 + 5 * (human_years - 2)]


def human_years_cat_years_dog_years1(human_years):
    cat_years = 15
    dog_years = 15
    if human_years >= 2:
        cat_years += 9 + 4 * (human_years - 2)
        dog_years += 9 + 5 * (human_years - 2)
    return [human_years, cat_years, dog_years]
