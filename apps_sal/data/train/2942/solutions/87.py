def fold_to(d,t = 0.0001):
    if 0 <= d <= t: 
        return 0
    elif d <= 0: 
        return None
        
    c = 0
    while t < d:
        c+=1
        t*=2
    return c
