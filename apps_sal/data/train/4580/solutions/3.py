def tiaosheng(arr):
    t = 0
    j = 0
    while t < 60:
        t += 1
        j += 1
        if j in arr:
            t += 3
    return j
