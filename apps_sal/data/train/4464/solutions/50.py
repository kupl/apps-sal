def feast(beast, dish):
    x = "".join(c for c in beast.split(" "))
    y = "".join(c for c in dish.split(" "))
    return (y[0] == x[0] and y[-1] == x[-1])
