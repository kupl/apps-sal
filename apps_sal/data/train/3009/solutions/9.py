def pairs(ar):
    a = []
    count = 0
    if len(ar) % 2 == 0:
        for i in range(0, len(ar), 2):
            if abs(ar[i] - ar[i + 1]) == 1:
                count += 1
    else:
        for i in range(0, len(ar) - 1, 2):
            if abs(ar[i] - ar[i + 1]) == 1:
                count += 1
    return count
