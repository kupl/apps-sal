def howmuch(m, n):
    i = min(m, n)
    j = max(m, n)
    res = []
    while (i <= j):
        if ((i % 9 == 1) and (i %7 == 2)):
            res.append(["M: " + str(i), "B: " + str(i // 7), "C: " + str(i // 9)])
        i += 1
    return res
