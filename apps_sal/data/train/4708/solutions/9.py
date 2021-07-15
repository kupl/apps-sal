def human_years_cat_years_dog_years(h):
    return [h, 15 + 9 * (h >= 2) + 4 * max(h - 2, 0), 15 + 9 * (h >= 2) + 5 * max(h - 2, 0)]
