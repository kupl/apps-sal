def gcd(a, b):
    if a == 0 or b == 0:
        if a == 0:
            return b
        else:
            return a
    else:
        return gcd(b, a % b)


def thegame(pos, cgcd):
    if pos == n:
        if cgcd == 1:
            return 1
        else:
            return 0
    elif (pos, cgcd) in dp:
        return dp[pos, cgcd]
    elif cgcd == 1:
        p = 2 ** (n - pos)
        dp[pos, cgcd] = p
        return p
    else:
        p = thegame(pos + 1, gcd(cgcd, nums[pos])) + thegame(pos + 1, cgcd)
        dp[pos, cgcd] = p
        return p


t = int(input())
while t > 0:
    n = int(input())
    nums = list(map(int, input().split()))
    dp = {}
    res = 0
    for pos in range(0, n - 1):
        res += thegame(pos + 1, nums[pos])
    print(res)
    t -= 1
