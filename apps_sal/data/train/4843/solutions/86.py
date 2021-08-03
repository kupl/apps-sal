def choose_best_sum(t, k, ls):
    import itertools

    sumList = []
    c = list(itertools.combinations(ls, k))  # find all combinations without repetition
    mySet = set(c)  # store combinations in unordered set

    for i in mySet:
        currentSum = sum(i)
        if currentSum <= t:
            sumList.append(currentSum)  # appends list if sum being iterated is less than or equal to limit

    if len(sumList) == 0:
        return None  # checks if there are any possible sums
    else:
        return max(sumList)  # returns greatest possible sum within given arguments
