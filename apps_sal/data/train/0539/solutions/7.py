from fractions import gcd
for _ in range(int(input())):
    n = int(input())
    s = n * 4
    m = n + 1
    if s % m == 0:
        print(s / m)
    else:
        print(s * m / gcd(s, m) / m)
