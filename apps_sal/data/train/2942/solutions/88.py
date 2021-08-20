def fold_to(distance):
    (n, count) = (0.0001, 0)
    while n < distance:
        (n, count) = (n * 2, count + 1)
    return None if distance < 0 else count
