#Try to make your own gcd method without importing stuff
def mygcd(a,b):
    if b == 0:
        return a
    else:
        return mygcd(b, a % b)
