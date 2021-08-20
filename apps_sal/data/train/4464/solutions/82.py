def feast(beast, dish):
    x = beast[0]
    y = dish[0]
    z = beast[-1]
    k = dish[-1]
    if x == y and z == k:
        return True
    else:
        return False
