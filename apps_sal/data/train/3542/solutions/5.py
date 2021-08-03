def owned_cat_and_dog(cat_years, dog_years):
    h1 = (cat_years > 14) + (cat_years > 23) + max(0, (cat_years - 24) // 4)
    h2 = (dog_years > 14) + (dog_years > 23) + max(0, (dog_years - 24) // 5)
    return [h1, h2]
