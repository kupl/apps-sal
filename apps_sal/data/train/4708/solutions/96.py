def human_years_cat_years_dog_years(h):
    return [h, 15 + (h >= 2) * (9 + (h - 2) * 4), 15 + (h >= 2) * (9 + (h - 2) * 5)]
