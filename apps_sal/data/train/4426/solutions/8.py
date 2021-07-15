def isMultiple(a, b, n):
    def rond(x):
        return int(x) if x % 1 < 0.5 else int(x + 1)
    
    res = a/b
    res = rond(res*10) / 10
    #Extra round here to deal with floating-point nonsense
    remainder = round(res % 1,1)
    return remainder and not (10*remainder) % n
