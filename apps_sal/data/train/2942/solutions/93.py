def fold_to(distance):
    folds = 0
    h = 0.0001
    while h < distance:
        h *= 2
        folds += 1
    return folds if distance >= 0 else None
