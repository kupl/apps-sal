for i in range(int(input())):

    def gcd(a, b):
        if a == 0:
            return b
        return gcd(b % a, a)

    def lcm(a, b):
        return a / gcd(a, b) * b
    (x, y) = map(int, input().split())
    lc = lcm(x, y)
    x = lc / x
    y = lc / y
    print(int(x + y - 2))
