def fold_to(distance):
    folds = 0
    thickness = 0.0001
    if distance < 0:
        return None
    else:
        while thickness < distance:
            thickness *= 2
            folds += 1
        return folds
