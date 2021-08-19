# cook your dish here
t = int(input())
while t:
    a, d, k, n, inc = map(int, input().split())
    n -= 1
    if inc and n >= k:
        a += (d * (k - 1))
        n -= (k - 1)
        d += inc
        while k <= n:
            a += (d * k)
            d += inc
            n -= k
    if n:
        a += (d * n)
    print(a)
    t -= 1
