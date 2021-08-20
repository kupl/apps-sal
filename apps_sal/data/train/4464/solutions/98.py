def feast(beast, dish):
    l1 = len(beast) - 1
    l2 = len(dish) - 1
    return beast[0] == dish[0] and beast[l1] == dish[l2]
