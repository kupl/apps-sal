def mygcd(a, b):
    if b == 0:
        return a
    else:
        return mygcd(b, a % b)
