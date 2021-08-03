# cook your dish here
t = int(input())
while t > 0:
    n, m = list(map(int, input().split()))
    p = n // m
    m %= 10
    q = (2 * m) % 10
    r = 1
    sm = m
    while q != m:
        sm += q
        q += m
        q %= 10
        r += 1
    sm *= (p // r)
    p %= r
    q = m
    while p > 0:
        sm += q
        q += m
        q %= 10
        p -= 1
    print(sm)
    t -= 1
