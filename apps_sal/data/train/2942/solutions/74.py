def fold_to(distance):
    if distance < 0:
        return None
    n = 0.0001
    cnt = 0
    while n < distance:
        n = n*2
        cnt += 1
    return cnt
