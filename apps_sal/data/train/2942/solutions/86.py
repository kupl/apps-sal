def fold_to(distance):
    paper = 0.0001
    folds = 0
    if distance < 0:
        return None
    distance -= paper
    while distance > 0:
        distance -= paper
        paper *= 2
        folds += 1
    return folds
