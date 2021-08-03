def owned_cat_and_dog(cat_years, dog_years):
    c, d = 0, 0
    if cat_years < 15:
        c = 0
    elif 15 <= cat_years < 24:
        c = 1
    elif cat_years == 24:
        c = 2
    else:
        c = (cat_years - 24) // 4 + 2
    if dog_years < 15:
        d = 0
    elif 15 <= dog_years < 24:
        d = 1
    elif dog_years == 24:
        d = 2
    else:
        d = (dog_years - 24) // 5 + 2
    return [c, d]
