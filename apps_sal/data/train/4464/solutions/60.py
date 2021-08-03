def feast(beast, dish):
    firstletter = beast[0]
    lastletter = beast[-1]
    firstletterdish = dish[0]
    lastletterdish = dish[-1]
    return (firstletter, lastletter) == (firstletterdish, lastletterdish)
