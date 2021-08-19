import math
for _ in range(int(input())):
    (n, m) = list(map(int, input().split()))
    t = math.gcd(n, m)
    t2 = n * m // t
    print(t2 // n - 1 + t2 // m - 1)
