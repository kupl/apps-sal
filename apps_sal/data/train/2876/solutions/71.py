def check(a, x):
    if len(a) == 1:
        return a[0] == x
    return a[0] == x or check(a[1:], x)
