def printn(x):
    return print(x, end='')


def inn():
    return int(input())


def inl():
    return list(map(int, input().split()))


def inm():
    return map(int, input().split())


def ins():
    return input().strip()


DBG = True
BIG = 10 ** 18
R = 998244353


def ddprint(x):
    if DBG:
        print(x)


(n, k) = inm()
dp = [[0] * (n + 1) for i in range(n + 1)]
dp[0][0] = 1
for i in range(1, n + 1):
    for j in range(i, 0, -1):
        dp[i][j] = (dp[i - 1][j - 1] + (dp[i][2 * j] if 2 * j <= i else 0)) % R
print(dp[n][k])
