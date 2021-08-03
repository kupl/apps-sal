def sum_dig_pow(a, b):
    l = []
    for i in range(a, b + 1):
        k = 0
        p = str(i)
        for j in range(len(p)):
            k += int(p[j]) ** (j + 1)
        if k == i:
            l.append(i)
    return l
