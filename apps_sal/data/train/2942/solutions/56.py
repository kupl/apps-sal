def fold_to(distance):
    
    if distance < 0 :
        return None
    
    a = 0
    
    while distance >= .0001 :
        distance /= 2
        a += 1
    
    return a

