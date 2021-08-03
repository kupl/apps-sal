def two_highest(x):
    if (type(x) == type("cool")):
        return False
    print(x)
    x.sort()
    x.reverse()
    i = 0
    if len(x) > 1:
        while x[i] == x[0]:
            i += 1
        return [x[0], x[i]]
    else:
        return x
