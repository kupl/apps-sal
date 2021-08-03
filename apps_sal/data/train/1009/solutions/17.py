def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


t = int(input())
while t > 0:
    t = t - 1
    n = int(input())
    L = list(map(int, input().split()))
    d = [1] + [0] * (10**4)
    for i in L:
        for j in range(1, (10**4) + 1):
            if d[j]:
                d[gcd(min(i, j), max(i, j))] += d[j]
        d[i] += 1
    print(d[1])
