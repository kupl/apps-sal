def gcd(a, b):
    return a if b == 0 else gcd(b, a % b)


def mn_lcm(m, n):
    if n < m:
        m, n = n, m
    ans = m
    for i in range(m, n + 1):
        ans = ((i * ans)) / (gcd(i, ans))
    return ans
