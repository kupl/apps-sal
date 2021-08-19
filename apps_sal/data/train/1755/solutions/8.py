# we get the least difference between the two lists if the sums are equal, i.e. each lists sum is half the the sum of the
# entire list. If we can't achieve that, we get as close to that target as possible. In other words, the solution uses the knapsack
# problem, in particular subset sum. We have a bag that has a capacity sum(lst)/2 which we are trying to fill as much as possible
# using elements from lst

def splitlist(lst):

    if not lst:
        return ([], [])
    target = sum(lst) // 2

    # dp array for knapsack problem
    dp = [[0 for _ in range(target + 1)] for _ in range(len(lst) + 1)]

    for i in range(1, len(lst) + 1):
        for j in range(target + 1):
            if j >= lst[i - 1]:

                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - lst[i - 1]] + lst[i - 1])

            else:
                dp[i][j] = dp[i - 1][j]

    seg1 = []

    w = target
    # get the values of the items in the first segment (the items which we used to get our max capacity in dp array)
    for i in range(len(lst), -1, -1):
        if dp[i][w] - dp[i - 1][w - lst[i - 1]] == lst[i - 1]:
            seg1.append(lst[i - 1])
            w -= lst[i - 1]

    # remove all items from list which belong to seg 1
    seg2 = [a for a in lst]
    for a in seg1:
        seg2.remove(a)

    return (seg1, seg2)
