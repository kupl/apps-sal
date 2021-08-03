def fold_to(distance):
    if distance < 0:
        return

    i = 0
    l = 0.0001
    while l < distance:
        l = l * 2
        i = i + 1
    return i
