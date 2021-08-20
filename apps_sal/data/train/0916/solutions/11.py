def gcd(a, b):
    if a == 0:
        return b
    return gcd(b % a, a)


t = int(input())
while t:
    (n, m) = input().split()
    n = int(n)
    m = int(m)
    lcm = n * m / gcd(n, m)
    print(int(lcm))
    t -= 1
