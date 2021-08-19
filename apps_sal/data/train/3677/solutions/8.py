def filter_homogenous(arrays):
    k = []
    while arrays:
        x = arrays.pop()
        if x and all((type(x[0]) == type(i) for i in x[1:])):
            k.insert(0, x)
    return k
