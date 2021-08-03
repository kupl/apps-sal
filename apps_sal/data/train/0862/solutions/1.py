import sys

MOD = 10**9 + 7
for __ in range(eval(input())):
    n, m, k = list(map(int, sys.stdin.readline().split()))
    lists = list(map(int, sys.stdin.readline().split()))
    ans = 0
    for i in lists:
        msd = i / k
        if msd > m:
            jaddu = i - (m * k)
        else:
            jaddu = i % k
        ans += jaddu % MOD
    print(ans % MOD)
