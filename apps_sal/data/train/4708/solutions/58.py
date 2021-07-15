def human_years_cat_years_dog_years(human):
    cat = 0
    dog = 0
    if human >= 1:
        cat += 15
        dog += 15
    if human >= 2:
        cat += 9
        dog += 9
    if human >= 3:
        n = human - 2
        cat += n * 4
        dog += n * 5
    return [human,cat,dog]
