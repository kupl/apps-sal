def check(a, x):
    try:
        return x in a
    except TypeError:
        return x == a

