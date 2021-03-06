import sys
sys.setrecursionlimit(2147483647)
INF = float('inf')
MOD = 10 ** 9 + 7


def input():
    return sys.stdin.readline().rstrip()


def resolve():
    S = list(map(lambda c: ord(c) - ord('a'), input()))
    n = len(S)
    sigma = 26
    next = [[-1] * sigma for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for c in range(sigma):
            next[i][c] = i if S[i] == c else next[i + 1][c]
    dp = [INF] * (n + 1)
    dp[n] = 1
    character = [None] * (n + 1)
    character[n] = 0
    for i in range(n - 1, -1, -1):
        for c in range(sigma):
            length = 1 if next[i][c] == -1 else 1 + dp[next[i][c] + 1]
            if dp[i] > length:
                dp[i] = length
                character[i] = c
    res = []
    now = 0
    while 1:
        res.append(character[now])
        now = next[now][character[now]] + 1
        if now == 0:
            break
    res = ''.join(map(lambda x: chr(x + ord('a')), res))
    print(res)


resolve()
