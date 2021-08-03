def solve(s, gcd):
    if s % gcd:
        return -1
    for i in range(gcd, s):
        for j in range(gcd, s):
            if i + j == s and i % gcd == 0 and j % gcd == 0:
                return (i, j)
