def fold_to(distance):
    if distance < 0:
        return None
        
    thiccness = .0001
    folds = 0
    
    while thiccness < distance:
        thiccness = thiccness * 2
        folds = folds + 1
        
    return folds
        

