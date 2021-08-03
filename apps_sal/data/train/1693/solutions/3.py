v = int(input())
eps = 3


def ans(a):
    a.sort()
    if len(a) % 2 == 0:
        med = a[len(a) // 2]
    else:
        med = (a[len(a) // 2] + a[len(a) // 2 - 1]) // 2

    l = med - med // 2
    r = med + med // 2

    c1 = c2 = 0

    for i in a:
        if i >= l and i <= r:
            c1 += 1
        else:
            c2 += 1

    if c2 == 0:
        c2 = 0.0001

    if c1 / c2 <= eps:
        return "uniform"
    else:
        return "poisson"


for i in range(v):
    cur = [int(i) for i in input().split()]
    print(ans(cur))
