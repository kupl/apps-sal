def choose_best_sum(t, k, ls):
    import itertools
    sumList = []
    c = list(itertools.combinations(ls, k))
    mySet = set(c)
    for i in mySet:
        currentSum = sum(i)
        if currentSum <= t:
            sumList.append(currentSum)
    if len(sumList) == 0:
        return None
    else:
        return max(sumList)
