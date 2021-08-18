def check(a, x):
    return (x == a[0] or check(a[1:], x)) if a else False
