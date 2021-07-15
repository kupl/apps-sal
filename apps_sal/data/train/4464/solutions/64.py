def feast(beast, dish):
    return True if dish[0] == beast[0] and dish[len(dish) - 1] == beast[len(beast) -1] else False
