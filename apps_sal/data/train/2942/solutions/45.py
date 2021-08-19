def fold_to(distance):
    p = 0.0001
    if distance < 0:
        return None
    print(p)
    if p >= distance:
        return 0
    count = 0
    print(p)
    while p < distance:
        p += p
        count += 1
    return count
