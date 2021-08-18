def human_years_cat_years_dog_years(human_years):
    return [
        human_years,
        sum([15 if x == 1 else (9 if x == 2 else 4) for x in range(1, human_years + 1)]),
        sum([15 if x == 1 else (9 if x == 2 else 5) for x in range(1, human_years + 1)])
    ]
