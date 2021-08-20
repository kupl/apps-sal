def feast(beast, dish):
    x = len(beast)
    y = len(dish)
    if dish[0] == beast[0] and beast[x - 1] == dish[y - 1]:
        return True
    else:
        return False
    pass
