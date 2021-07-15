def feast(beast, dish):
    return beast[::len(beast)-1] == dish[::len(dish)-1]
