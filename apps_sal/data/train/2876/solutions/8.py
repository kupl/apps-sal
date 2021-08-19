def check(a, x):
    return a != [] and (a[0] == x or check(a[1:], x))
