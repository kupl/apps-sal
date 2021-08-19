def fold_to(distance):
    if distance < 0:
        return None
    res = 0
    l = 0.0001
    while l < distance:
        l *= 2
        res += 1
    return res
