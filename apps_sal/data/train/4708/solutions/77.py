def human_years_cat_years_dog_years(h):
    return [h, (h - 2) * 4 + 24 if h >= 2 else 15 if h == 1 else 24, (h - 2) * 5 + 24 if h >= 2 else 15 if h == 1 else 24]
