def check(a, x):
    return (x == a[0] or check(a[1:], x)) if a else False
    # return x in a # there is technically no loop
