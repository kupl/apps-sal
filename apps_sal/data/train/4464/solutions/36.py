def feast(beast, dish):
    return beast.startswith(dish[:1]) & beast.endswith(dish[-1])
