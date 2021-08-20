def check(a, x):
    try:
        if type(a.index(x)) == int or type(a.index(x)) == str:
            return True
        else:
            return False
    except ValueError:
        return False
