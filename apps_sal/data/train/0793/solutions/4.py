import math
(n, k) = map(int, input().split())
ls = list(map(int, input().split()))
ls.append(k)
ls.sort()
if len(ls) > 2:
    z = math.gcd(ls[1] - ls[0], ls[2] - ls[1])
    for i in range(3, len(ls)):
        z = math.gcd(ls[i] - ls[i - 1], z)
else:
    z = ls[1] - ls[0]
print(z)
