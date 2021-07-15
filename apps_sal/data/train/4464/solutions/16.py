def feast(beast, dish):
    return beast.endswith(dish[-1]) and beast.startswith(dish[0])
