def round_to_next5(n):
    i = 5
    while True:
        x = i - n
        if x in range(0, 5):
            return i
        elif x < 0:
            i = i + 5
        elif x >= 5:
            i = i - 5
    return n
