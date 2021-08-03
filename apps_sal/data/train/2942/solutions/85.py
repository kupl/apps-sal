def fold_to(distance):
    if distance < 0:
        return None
    d = distance // 0.0001
    i = 0
    while d > 0:
        d //= 2
        i += 1
    return i
