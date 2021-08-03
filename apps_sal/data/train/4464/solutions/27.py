def feast(beast, dish):
    x = beast[0] + beast[len(beast) - 1]
    y = dish[0] + dish[len(dish) - 1]
    if x == y:
        return True
    else:
        return False
