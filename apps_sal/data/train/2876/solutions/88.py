def check(a, x):
    try:
        a.remove(x)
        return True
    except:
        return False
