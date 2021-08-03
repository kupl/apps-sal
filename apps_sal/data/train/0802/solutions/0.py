import math


def csb(n):
    count = 0
    while (n):
        n &= (n - 1)
        count += 1

    return count


def f(ca, cb, i, cf, C, n, dp):
    if ca < 0 or cb < 0:
        return 0
    if i == n:
        if ca == 0 and cb == 0 and cf == 0:
            return 1
        return 0
    st = str(ca) + " " + str(cb) + " " + str(cf) + " " + str(i)
    if dp.get(st) != None:
        return dp[st]
    x = 0
    if (C & (1 << i)) > 0:
        x = 1
    if x == 1:
        # we will have odd num of set bits
        if cf == 1:
            dp[st] = f(ca, cb, i + 1, 0, C, n, dp) + f(ca - 1, cb - 1, i + 1, 1, C, n, dp)
        else:
            dp[st] = f(ca - 1, cb, i + 1, 0, C, n, dp) + f(ca, cb - 1, i + 1, 0, C, n, dp)
    else:
        if cf == 1:
            dp[st] = f(ca - 1, cb, i + 1, 1, C, n, dp) + f(ca, cb - 1, i + 1, 1, C, n, dp)
        else:
            dp[st] = f(ca, cb, i + 1, 0, C, n, dp) + f(ca - 1, cb - 1, i + 1, 1, C, n, dp)

    return dp[st]


def ip():

    for _ in range(int(input())):
        a, b, c = list(map(int, input().split()))
        n = int(math.log(c, 2)) + 1
        dp = {}
        print(f(csb(a), csb(b), 0, 0, c, n, dp))


ip()
