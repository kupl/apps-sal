import math
for i in range(int(input())):
    (n, m) = map(int, input().split())
    if n == m or n == 0 or m == 0:
        print(n + m)
    else:
        a = math.gcd(n, m)
        print(2 * a)
