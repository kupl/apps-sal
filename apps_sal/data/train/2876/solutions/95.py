def check(a, x):
    try:
        a.index(x)
    except:
        return False
    return True
