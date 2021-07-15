def splitlist(lst):
    if not lst:
        return ([], [])
    lst = sorted(lst, reverse=True)
    optimum = sum(lst) // 2
    if optimum <= lst[0]:
        return [lst[0]], lst[1:]
    dp = [None] * (optimum + 1)
    dp[0] = []
    for item in lst:
        for pos in reversed(range(optimum - item + 1)):
            if dp[pos] is not None and dp[pos + item] is None:
                dp[pos + item] = dp[pos] + [item]
    best = next(reversed([option for option in dp if option is not None]))
    for item in best:
        lst.remove(item)
    return best, lst
