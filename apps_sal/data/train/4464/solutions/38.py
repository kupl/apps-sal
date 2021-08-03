def feast(beast, dish):
    res = False
    return beast[0] == dish[0] and beast[len(beast) - 1] == dish[len(dish) - 1]
