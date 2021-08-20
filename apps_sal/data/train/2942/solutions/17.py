def fold_to(distance):
    print(distance)
    if distance == None:
        return 0
    if distance < 0:
        return None
    if distance == 0.0:
        return 0
    res = 0.0001
    folds = 0
    while res < distance:
        res *= 2
        folds += 1
    return folds
