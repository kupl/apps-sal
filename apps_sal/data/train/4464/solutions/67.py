def feast(beast, dish):
    # your code here
    return beast.startswith(dish[0]) and beast.endswith(dish[-1])
    # don't have to put True or False, as if they will return means its true
