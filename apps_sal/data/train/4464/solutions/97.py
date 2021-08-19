def feast(beast, dish):
    print(beast, dish)
    # your code here
    return dish.startswith(beast[0]) and dish.endswith(beast[-1])
