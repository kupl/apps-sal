# cook your dish here - pyt3
def fun(a):
    t1 = 1
    t2 = a
    p = a - 1
    pday = 1
    count = 1
    while t2 > t1:
        t2 += a
        t1 = 1 + (2 * t1)
        if t2 - t1 > p:
            p = max(p, t2 - t1)
            pday = count
        count += 1
    return count - 1, pday + 1


try:
    t = int(input())
    for i in range(t):
        n = int(input())
        x = fun(n)
        print(x[0], x[1])
except Exception:
    pass
