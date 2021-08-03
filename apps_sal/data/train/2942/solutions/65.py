def fold_to(distance):
    thick = 0.0001

    if distance < 0:
        return None

    elif thick > distance:
        return 0

    else:
        counter = 0
        while thick < distance:
            thick = thick * 2
            counter += 1

    return counter
