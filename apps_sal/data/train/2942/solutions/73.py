def fold_to(distance):
    thickness = 0.0001
    folds = 0

    if distance < 0:
        return None

    elif distance < thickness:
        return 0

    else:
        while thickness < distance:
            thickness = thickness * 2
            folds = folds + 1

            if thickness >= distance:
                return int(folds)
