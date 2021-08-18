def fold_to(distance):
    i = 0.0001
    n = 0
    if distance < 0:
        return None
    while i < distance:
        i = i * 2
        n += 1
    return n
