def fold_to(distance):
    if distance < 0:
        return None
    for i in range(0, 10000):
        if 2 ** i * 0.0001 >= distance:
            return i
