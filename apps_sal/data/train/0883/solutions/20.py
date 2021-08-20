for _ in range(int(input())):
    a = int(input())
    x = list(map(int, input().split()))
    y = set(x)
    z = list((k for k in y))
    if len(z) == 1:
        if z[0] == 0:
            f = a
        elif z[0] == a - 1:
            f = 0
        else:
            f = -1
    elif len(y) == 2:
        for r in range(0, a + 1):
            t = [r] * (a - r) + [r - 1] * r
            if sorted(t) == sorted(x):
                f = a - max(z)
                break
            else:
                f = -1
    else:
        f = -1
    print(f)
