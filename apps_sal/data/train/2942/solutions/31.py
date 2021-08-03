def fold_to(distance):
    if distance < 0:
        return None
    length = 0.0001
    count = 0
    while length <= distance:
        length *= 2
        count += 1
    return count
