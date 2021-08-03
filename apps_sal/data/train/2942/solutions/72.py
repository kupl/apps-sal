def fold_to(distance):
    i = 0
    while distance > 0.00010:
        distance = distance / 2
        i += 1

    return i if distance >= 0 else None
