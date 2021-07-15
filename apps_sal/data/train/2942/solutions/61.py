def fold_to(distance):
    if distance < 0:
        return None
    if distance < 0.0001:
        return 0
    counter = 0
    while distance > 0.0001:
        distance /= 2
        counter += 1
    return counter

