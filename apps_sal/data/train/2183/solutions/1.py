import sys
input = sys.stdin.readline

MOD = 10**9 + 7
t = int(input())

for _ in range(t):
    x = int(input())
    s = list(input())
    n = len(s) - 1
    for i in range(n):
        s[i] = int(s[i])

    memo = {}
    for i in range(n):
        memo[i] = s[i]

    ans = len(memo)
    pos = i + 1
    for i in range(x):
        tmp = pos
        if tmp <= x:
            for j in range(memo[i] - 1):
                for k in range(i + 1, pos):
                    memo[tmp] = memo[k]
                    tmp += 1
            pos = tmp
            ans = tmp
        else:
            ans = ans + (ans - i - 1) * (memo[i] - 1)
            ans %= MOD
    print(ans % MOD)
