def owned_cat_and_dog(cat_years, dog_years):
    i = cat_years
    k = dog_years
    if i < 24:
        cat_years = 1
    if k < 24:
        dog_years = 1
    if i == 24:
        cat_years = 2
    if k == 24:
        dog_years = 2
    if i > 24:
        cat_years = int((i - 24) / 4) + 2
    if k > 24:
        dog_years = int((k - 24) / 5) + 2
    if i < 15:
        cat_years = 0
    if k < 15:
        dog_years = 0
    return [cat_years, dog_years]
