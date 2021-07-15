def fold_to(distance):
    thickness = 0.0001
    if distance < 0:
        return None
    i = 0
    while thickness < distance:
        thickness *= 2
        i += 1
    return i
