import math
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a = list(set(a))
    x, p = 0, 0
    z = max(a)
    a.remove(z)
    for i in range(len(a)):
        x = math.gcd(x, a[i])

    y = max(a)
    a.append(z)
    a.remove(y)
    for i in range(len(a)):
        p = math.gcd(p, a[i])
    print(max(z + x, p + y))
