def mygcd(x,y):
    return x if not y else mygcd(y, x%y)
