def human_years_cat_years_dog_years(human_years):
    animal_first_two_years = 15 if human_years > 0 else 0
    animal_first_two_years += 9 if human_years > 1 else 0
    animal_last_years = max(0, human_years - 2)
    return [
        human_years,
        animal_first_two_years + 4 * animal_last_years,
        animal_first_two_years + 5 * animal_last_years,
    ]
