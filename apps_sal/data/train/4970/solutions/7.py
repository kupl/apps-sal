def vampire_test(x, y):
    m = str(x * y)
    x = str(x) + str(y)
    if set(m) == set(x) and len(x) == len(m):
        return True
    return False
