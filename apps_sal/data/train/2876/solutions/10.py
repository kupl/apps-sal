def check(a, x): 
    if a:
        if a[0] == x:
            return(True)
        else:
            return(check(a[1:], x))
    else: 
        return(False)
    pass
