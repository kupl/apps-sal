def fold_to(distance):
    paperThickness = 0.0001
    folds = 0
    if distance < 0:
        return None
    while paperThickness < distance:
        paperThickness *= 2
        folds += 1
    return folds
