def monkey_count(n):

    # set up empty list
    monkeyCount = []

    # for all numbers up to n, add to list
    for i in range(n):
        monkeyCount.append(i + 1)

    return(monkeyCount)
