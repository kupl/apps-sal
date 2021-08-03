def owned_cat_and_dog(cat, dog):
    import math
    return list(map(math.floor, [
        cat / 15 if cat < 24 else (cat - 16) / 4,
        dog / 15 if dog < 24 else (dog - 14) / 5
    ]))
