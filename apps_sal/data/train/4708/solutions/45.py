def human_years_cat_years_dog_years(y):
    return [y, y * 4 + (16 if y > 1 else 11 if y == 1 else 0), y * 5 + (14 if y > 1 else 10 if y == 1 else 0)]
