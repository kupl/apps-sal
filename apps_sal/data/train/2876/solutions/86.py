def check(a, x):
    if len(a) == 0:
        return False
    if a[0] == x:
        return True
    else:
        return check(a[1:], x)
    return False
