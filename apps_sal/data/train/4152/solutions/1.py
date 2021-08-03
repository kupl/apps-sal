def mygcd(x, y):
    return x if y == 0 else mygcd(y, x % y)
