def fold_to(distance):
    a = 0
    n = 0.0001
    if distance < 0:
        return None
    while n < distance:
        n *= 2
        a += 1
    return a
