check = lambda a, x: a != [] and (a[0] == x or check(a[1:], x))
