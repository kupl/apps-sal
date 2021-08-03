def feast(beast, dish):
    return (dish.startswith(beast[0]) and dish.endswith(beast[len(beast) - 1]))
