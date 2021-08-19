# Try to make your own gcd method without importing stuff
def mygcd(x, y):
    # GOOD LUCK
    while y:
        x, y = y, x % y
    return x
