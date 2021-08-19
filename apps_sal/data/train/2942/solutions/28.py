def fold_to(distance):
    if distance < 0:
        return None
    elif distance == 0:
        return 0
    else:
        folds = 0
        thickness = 0.0001
        while thickness <= distance:
            thickness *= 2
            folds += 1
    return folds
    # your code here
