def check(a, x): 
    try:
        exists = a.index(x)
        return True
    except:
        return False
