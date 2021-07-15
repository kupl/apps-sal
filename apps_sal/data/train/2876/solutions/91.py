def check(a, x): 
    try:
       a.index(x)
    except ValueError:
       return False
    return True
