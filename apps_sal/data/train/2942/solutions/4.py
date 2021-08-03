def fold_to(distance):
    const = 0.0001
    if distance < 0:
        return None
    elif distance < const:
        return 0
    fold = 0
    while distance > const * 2**fold:
        fold += 1
    return fold
