MOD = 10 ** 9 + 7


def main():
    t = int(input())
    for i in range(t):
        s = list(map(int, input()))
        (p, m) = (0, 1)
        for d in reversed(s):
            p += d * m
            m = m * 10 % MOD
        r = 0
        for d in s:
            r = (r * m + p) % MOD
            p = (p * 10 - (m - 1) * d) % MOD
        print(r)


main()
