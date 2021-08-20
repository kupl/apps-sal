def fold_to(distance):
    if distance < 0:
        return None
    i = 0.0001
    count = 0
    if distance == 0:
        return 0
    while distance > i:
        distance = distance / 2
        count += 1
    return count
