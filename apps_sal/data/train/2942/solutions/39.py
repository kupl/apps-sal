def fold_to(distance):
    d = 0.0001
    c = 0
    if distance < 0:
        return None
    while d < distance:
        d = d * 2
        c += 1
    return c
