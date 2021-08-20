def upd(ary, nary):
    tt = ary + nary
    tt.sort()
    return [tt[-2], tt[-1]]


def main1(n, a):
    dp = [[a[i], 0] for i in range(1 << n)]
    for j in range(n):
        bit = 1 << j
        for i in range(2 ** n):
            if i & bit == 0:
                dp[i | bit] = upd(dp[i ^ bit], dp[i])
    pre = 0
    for (x, y) in dp[1:]:
        pre = max(pre, x + y)
        print(pre)


n = int(input())
a = list(map(int, input().split()))
main1(n, a)
