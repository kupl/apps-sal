def fold_to(distance):
    if (distance < 0):
        return None
    folds = 0
    while (0.0001 < distance):
        folds += 1
        distance /= 2
    return folds
