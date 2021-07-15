def human_years_cat_years_dog_years(human_years):
    return [human_years, *(dict(enumerate((15, 24))).get(human_years - 1, k * (human_years - 2) + 24) for k in (4, 5))]
