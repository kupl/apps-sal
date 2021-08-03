def check(a, x):
    b = a
    try:
        return not a == b.remove(x)
    except:
        return False
