def human_years_cat_years_dog_years(human_years):
    if human_years == 1:
        dog = 15
        cat = 15
    elif human_years == 2:
        dog = 24
        cat = 24
    else:
        dog = 24 + (int(human_years - 2) * 5)
        cat = 24 + (int(human_years - 2) * 4)
    return [human_years,cat,dog]
