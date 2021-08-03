def fold_to(distance):
    if distance < 0:
        return None
    i = 0
    while (0.0001) * 2 ** i < distance:
        i += 1
    return i
