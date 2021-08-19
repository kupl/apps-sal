def fold_to(distance):
    position = 0.0001
    folds = 0
    while position < distance:
        position = position * 2
        folds += 1
    if distance < 0:
        return None
    else:
        return folds
