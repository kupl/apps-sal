def f(k, n):
    memo = [1]
    for i in range(1,n+1): memo.append(memo[-1]+memo[i//k])
    return memo[-1]
