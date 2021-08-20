def feast(beast, dish):
    print(beast, dish)
    return dish.startswith(beast[0]) and dish.endswith(beast[-1])
