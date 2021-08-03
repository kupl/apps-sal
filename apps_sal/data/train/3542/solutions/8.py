def owned_cat_and_dog(cat_years, dog_years):
    cat = 0 if cat_years < 15 else 1 if cat_years < 24 else (cat_years - 16) // 4
    dog = 0 if dog_years < 15 else 1 if dog_years < 24 else (dog_years - 14) // 5
    return [cat, dog]
