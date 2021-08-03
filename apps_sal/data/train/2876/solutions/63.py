def check(a, x):
    try:
        if type(a.index(x)) == int:
            return True
        else:
            return False
    except ValueError:
        return False
