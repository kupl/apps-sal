def fold_to(distance):
    p = 0.0001
    n = 0
    while p <= distance:
        p = p * 2
        n += 1
    if distance < 0:
        return None
    else:
        return n
    # your code here
