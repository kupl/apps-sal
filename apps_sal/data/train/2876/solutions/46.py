def check(a, x): 
    try:
        return True if a.index(x) != -1 else False
    except:
        return False
