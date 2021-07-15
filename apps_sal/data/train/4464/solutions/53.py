def feast(beast, dish):
    if dish[len(dish)-1] != beast[len(beast)-1] and beast[0] != dish[0]:
        return False
    if dish[len(dish)-1] == beast[len(beast)-1] and beast[0] == dish[0]:
        return True
    else:
        return False
