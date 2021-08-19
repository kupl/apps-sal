def fold_to(distance):
    x = 0.0001
    count = 0
    if distance > x:
        while x < distance:
            x += x
            count += 1
        return count
    elif distance < 0:
        return None
    return 0
