def addsup(a1, a2, a3):
    sums = []
    for i in a1:
        for j in a2:
            if (i + j) in a3:
                sums.append([i, j, i + j])
    return sums
