def human_years_cat_years_dog_years(x):
    return [x, 24 + (x - 2) * 4 if (x != 1) else 15, 24 + (x - 2) * 5 if (x != 1) else 15]
