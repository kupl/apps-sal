def fold_to(distance):
    n = 0
    results = 0
    if 0.0001 < distance:
        while results < distance:
            n += 1
            results = 0.0001 * 2 ** n
        return n
    if distance < 0:
        return None
    if 0.0001 > distance:
        return 0
