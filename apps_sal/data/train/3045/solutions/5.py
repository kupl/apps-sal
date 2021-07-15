def elevator(x, y, r):
    return ['left','right'][abs(r-x)>=abs(r-y)]
