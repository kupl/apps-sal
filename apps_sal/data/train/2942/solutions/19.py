def fold_to(distance):
    folds = 0
    thickness = 0.0001
    total = 0

    if distance >= 0:
        while thickness < distance:
            thickness *= 2
            folds += 1

    else:
        return None

    return folds
