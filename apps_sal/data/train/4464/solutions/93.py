def feast(beast, dish):
    is_valid = True
    if beast[0] == dish[0] and beast[len(beast) - 1] == dish[len(dish) - 1]:
        is_valid = True
        return is_valid
    else:
        is_valid = False
        return is_valid

