def fold_to(distance):
    fold, thickness = 0, 0.0001;
    if distance < 0: return(None)
    while thickness <= distance:
        thickness *= 2
        fold += 1
    return(fold)
