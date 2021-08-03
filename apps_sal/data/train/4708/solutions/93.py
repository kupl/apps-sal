def human_years_cat_years_dog_years(h):
    return [h, 15 + 9 * int(h > 1) + 4 * (h - 2) * int(h > 2), 15 + 9 * int(h > 1) + 5 * (h - 2) * int(h > 2)]
