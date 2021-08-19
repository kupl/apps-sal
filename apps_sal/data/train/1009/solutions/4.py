def cal(a, b):
    if b == 0:
        return a
    return cal(b, a % b)


def func(pos, cur_gcd):
    if pos == n:
        if cur_gcd == 1:
            return 1
        else:
            return 0
    if (pos, cur_gcd) in dp:
        return dp[pos, cur_gcd]
    if cur_gcd == 1:
        ans = 2 ** (n - pos)
        dp[pos, cur_gcd] = ans
        return ans
    ans = func(pos + 1, cal(cur_gcd, a[pos])) + func(pos + 1, cur_gcd)
    dp[pos, cur_gcd] = ans
    return ans


for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    dp = dict()
    ans = 0
    for (i, j) in enumerate(a):
        ans += func(i + 1, j)
    print(ans)
