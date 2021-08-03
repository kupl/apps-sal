from functools import partial


def human_years_cat_years_dog_years(human_years):
    return [age_func(human_years) for age_func in (human_age, cat_age, dog_age)]


def critter_age(human_years, critter_years_multipliers):
    critter_age = previous_year = 0
    for year, multiplier in critter_years_multipliers:
        is_older = human_years > year
        years_difference = (year if is_older else human_years) - previous_year
        critter_age += multiplier * years_difference
        if not is_older:
            break
        previous_year = year
    return critter_age


infinity = float('inf')

human_age = partial(critter_age, critter_years_multipliers=((infinity, 1),))
cat_age = partial(critter_age, critter_years_multipliers=((1, 15),
                                                          (2, 9),
                                                          (infinity, 4)))
dog_age = partial(critter_age, critter_years_multipliers=((1, 15),
                                                          (2, 9),
                                                          (infinity, 5)))
