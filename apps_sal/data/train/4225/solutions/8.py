def cup_and_balls(b, a):
    for (i, j) in a:
        if b == i:
            b = j
        elif b == j:
            b = i
    return b
