from collections import defaultdict


def factorial(n):
    if n < 0:
        return 0
    elif n == 0 or n == 1:
        return 1
    else:
        fact = 1
        while(n > 1):
            fact *= n
            n -= 1
        return fact


m = pow(10, 9) + 7
for _ in range(int(input())):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    d = defaultdict(int)
    d[0] = 1
    ans = 1
    ex = 0
    for i in a:
        d[i] = d[i] + 1
    for i in range(1, max(a) + 1):
        ans = (ans * pow(d[i - 1], d[i], m)) % m
        ex = ex + int((d[i] * (d[i] - 1)) / 2)
    if(k > n - 1):
        t = k - (n - 1)
        if(t > ex):
            ans = 0
        else:
            ans = (ans * factorial(ex) / (factorial(ex - t) * factorial(t)) % m) % m
    print(ans)
