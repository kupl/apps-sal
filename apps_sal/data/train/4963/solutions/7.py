def closest_multiple_10(i):
    for j in range(int(i - 5), int(i + 6)):
        if j % 10 == 0:
            i = j
    return i
