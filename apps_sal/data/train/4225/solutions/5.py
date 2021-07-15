def cup_and_balls(b, arr):
    cups = [0] * 4
    cups[b] = 1
    for i, j in arr:
        cups[i], cups[j] = cups[j], cups[i]
    return cups.index(1)
