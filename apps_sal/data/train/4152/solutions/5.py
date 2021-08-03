def mygcd(x, y):
    if x == 0:
        return y
    if y == 0:
        return x
    else:
        return mygcd(y, x % y)
