def fold_to(distance):
    if distance < 0:
        return None
    count = 0
    paper = 0.0001
    while paper < distance:
        count += 1
        paper *= 2
    return count
