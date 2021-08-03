def check(a, x):
    try:
        i = a.index(x)
        return True
    except ValueError:
        return False
