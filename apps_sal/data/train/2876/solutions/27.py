
def check(a, x):
    if not a:
        return False
    if a[0] == x:
        return True
    else:
        return check(a[1:], x)
