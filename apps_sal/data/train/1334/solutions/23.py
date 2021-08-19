from sys import stdin, stdout


def fn(pos):
    if pos >= n:
        return 0
    if pos in dp:
        return dp[pos]
    op1 = op2 = op3 = float('inf')
    op1 = a[pos] + fn(pos + 3)
    if pos + 1 < n:
        op2 = a[pos + 1] + fn(pos + 3)
    if pos + 2 < n:
        op3 = a[pos + 2] + fn(pos + 3)
    dp[pos] = min(op1, op2, op3)
    return dp[pos]


for _ in range(1):  # int(stdin.readline())):
    n = int(stdin.readline())
    a = list(map(int, stdin.readline().split()))
    # print(dp)
    dp = [0] * n
    dp[0] = a[0]
    if n == 1:
        print(dp[0])
        continue
    dp[1] = a[1]
    if n == 2:
        print(min(dp))
        continue
    dp[2] = a[2]
    if n == 3:
        print(min(dp))
        continue
    for i in range(3, n):
        dp[i] = min(dp[i - 3], dp[i - 1], dp[i - 2]) + a[i]
    print(min(dp[-1], dp[-2], dp[-3]))
