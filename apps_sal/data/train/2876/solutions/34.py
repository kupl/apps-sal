def check(a, x):
    try:
        if x in a:
            return True
        elif str(x).lower in a:
            return True
    except ValueError:
        return False
    else:
        return False
