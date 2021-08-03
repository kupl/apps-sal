def cup_and_balls(b, arr):
    for i in arr:
        if b in i:
            b = sum(i) - b
    return b
