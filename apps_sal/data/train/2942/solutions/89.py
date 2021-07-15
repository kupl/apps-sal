def fold_to(d):
    folds = 0
    t = 0.0001;
    if d < 0: return(None)
    while t <= d:
        t = t*2
        folds += 1
    return (folds)
    
    
    

