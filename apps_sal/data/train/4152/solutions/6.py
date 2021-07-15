def mygcd(x,y):
    """Euclidean algorithm."""
    reminder = x%y
    if reminder == 0:
        return y
    else:
        return mygcd(y,reminder)
