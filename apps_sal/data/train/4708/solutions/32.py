def human_years_cat_years_dog_years(h):
    cat = sum([15 if x == 0 else 9 if x == 1 else 4 for x in range(h)])
    return [h, cat, cat + h - 2 if h > 2 else cat]
