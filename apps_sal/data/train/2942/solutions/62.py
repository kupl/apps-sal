def fold_to(distance):
    if distance < 0:
        return None
    thickness = 0.0001
    n = 0
    while thickness * 2 ** n < distance:
        n += 1
    return n
