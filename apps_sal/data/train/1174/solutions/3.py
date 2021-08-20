def f(n):
    c = 0
    while n:
        n = n & n - 1
        c ^= 1
    return c


mod = 10 ** 9 + 7
for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    (od, ev) = (0, 0)
    for i in l:
        if f(i):
            od += 1
        else:
            ev += 1
    (p, q) = (0, 0)
    if od >= 3:
        p = od * (od - 1) * (od - 2)
        p = p // 6
    if ev >= 2 and od > 0:
        q = ev * (ev - 1)
        q = q >> 1
        q = q * od
