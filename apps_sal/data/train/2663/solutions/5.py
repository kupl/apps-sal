def addsup(a1, a2, a3):
    sums = []
    # test every possible combination of a1 and a2, if sum in a3, append to result list
    for i in a1:
        for j in a2:
            if (i + j) in a3:
                sums.append([i, j, i + j])
    return sums
