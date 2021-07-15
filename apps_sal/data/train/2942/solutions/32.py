def fold_to(distance):
    if distance < 0: return None
    length, count = 0.0001, 0
    while length <= distance:
        length *= 2
        count += 1
    return count
