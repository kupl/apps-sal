def feast(beast, dish):
    return True if beast[::len(beast)-1] == dish[::len(dish)-1] else False
