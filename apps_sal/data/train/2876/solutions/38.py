def check(a, x): 
    try:
        a.index(x)
        return True
    except:
        return False
