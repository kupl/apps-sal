MOD = pow(10, 9) + 7


def solve(s):
    n = len(s)
    a = [25 - (ord(x) - 65) for x in s]
    (r, s) = (0, 0)
    for i in range(n):
        r = (r + a[i] + s * a[i]) % MOD
        s = (a[i] + s * 26) % MOD
    return r
