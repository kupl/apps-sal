n = int(input())
a = list(map(int, input().split()))
dp = [[0, 0] for i in range(1 << n)]


def merge(ls1, ls2):
    (p, q) = ls1
    (r, s) = ls2
    ret = [max(p, r)]
    if p > r:
        ret.append(max(q, r))
    else:
        ret.append(max(p, s))
    return ret


for i in range(1 << n):
    dp[i][0] = a[i]
for i in range(n):
    for j in range(1 << n):
        if 1 << i & j:
            dp[j] = merge(dp[j], dp[1 << i ^ j])
ans = [0 for i in range(2 ** n)]
for i in range(1, 1 << n):
    ans[i] = max(ans[i - 1], sum(dp[i]))
for i in ans:
    if i:
        print(i)
