def human_years_cat_years_dog_years(human_years):
    a = 15 + 9 * int(human_years >> 1 != 0)
    return [human_years, a + 4 * max(0, (human_years - 2)), a + 5 * max(0, (human_years - 2))]
