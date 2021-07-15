def fold_to(distance):
    count=0
    if distance < 0:
        return None
    thickness=0.0001
    if distance < thickness:
        return 0
    while thickness < distance:
        thickness *= 2
        count += 1
    return count

