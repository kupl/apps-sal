def check(a, x): 
    try:
        if a.count(a.index(x)) >= 0:
            return True
        else:
            return False
    except ValueError:
        return False
