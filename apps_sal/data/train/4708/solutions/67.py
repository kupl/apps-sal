def human_years_cat_years_dog_years(h):
    (cat, dog) = (0, 0)
    if h >= 1:
        cat += 15
        dog += 15
    if h >= 2:
        cat += 9
        dog += 9
    if h >= 3:
        cat += 4 * (h - 2)
        dog += 5 * (h - 2)
    return [h, cat, dog]
