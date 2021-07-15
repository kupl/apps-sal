def array_madness(a,b):
    x = 0
    for k in a:
        x += k**2
    
    y = 0
    for k in b:
        y += k**3
    
    if x > y:
        return True
    else:
        return False
    # Ready, get, set, GO!!!

