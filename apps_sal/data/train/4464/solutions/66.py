def feast(beast, dish):
    dish_allowed = beast[0] == dish[0] and beast[-1] == dish[-1]
    return dish_allowed
