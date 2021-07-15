def fold_to(distance):
    fold=0.0001
    
    if distance <=-1:
        return None
    elif distance < fold:
        return 0
    i=0
    while fold<=distance:
        fold=fold*2
        i+=1
    return i
