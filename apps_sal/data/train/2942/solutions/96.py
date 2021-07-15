def fold_to(distance):
    if distance < 0: 
        return None
        
    res = 0
    d = 0.0001
    while d < distance: 
        d *= 2
        res +=1
    return res
