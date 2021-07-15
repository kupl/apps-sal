def filter_homogenous(arrays):
    f = lambda x: type(x[0])
    k = []
    while arrays:
        x = arrays.pop()
        if x and all(f(x)==type(i) for i in x ):
            k.insert(0,x)
    return k

