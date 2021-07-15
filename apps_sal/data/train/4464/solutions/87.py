def feast(beast, dish):
    beast = beast.lower()
    dish = dish.lower()
    return beast[0] == dish[0] and beast[-1] == dish[-1]
