def partitions(n):
    part = [0] * (n + 1)
    part[0] = 1
    for i in range(1, n + 1):
        for j in range(i, n + 1):
            part[j] += part[j - i]
    return part[-1]
