def tidyNumber(n,p=''):
    for s in str(n):
        if(s < p): return False 
        else: p = s

    return True
