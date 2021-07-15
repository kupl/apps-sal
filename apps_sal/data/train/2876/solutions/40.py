def check(a, x):
    try:
        if x in a or x.lower() in a.lower():
            return True
        else:
            return False
    except AttributeError:
        return False
