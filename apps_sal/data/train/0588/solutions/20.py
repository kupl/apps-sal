def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(i) for i in input().split()]
    x = []
    for i in range(1, n):
        x.append(a[i] - a[i - 1])
    x.append(360 - a[n - 1] + a[0])
    p = x[0]
    s = 0
    for i in x:
        p = gcd(p, i)
    for i in x:
        s += i // p - 1
    print(s)
