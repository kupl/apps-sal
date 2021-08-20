import math
t = int(input())


def phi(n):
    res = n
    i = 2
    while i * i <= n:
        if n % i == 0:
            res /= i
            res *= i - 1
            while n % i == 0:
                n /= i
        i += 1
    if n > 1:
        res /= n
        res *= n - 1
    return int(res)


while t:
    (a, m) = list(map(int, input().split()))
    g = math.gcd(a, m)
    print(phi(m // g))
    t -= 1
