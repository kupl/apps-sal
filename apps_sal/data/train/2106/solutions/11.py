def rr():
    return input().strip()


def rri():
    return int(rr())


def rrm():
    return [int(x) for x in rr().split()]


def sol(n):
    cm = []
    res1 = 0
    res2 = 0
    for i in range(n):
        x = rrm()
        if x[0] % 2 == 1:
            cm.append(x[x[0] // 2 + 1])
        res1 += sum(x[1:x[0] // 2 + 1])
        res2 += sum(x[(x[0] + 1) // 2 + 1:])
    cm.sort(reverse=True)
    for (i, v) in enumerate(cm):
        if i % 2 == 0:
            res1 += v
        else:
            res2 += v
    return str(res1) + ' ' + str(res2)


T = 1
for _ in range(T):
    n = rri()
    ans = sol(n)
    print(ans)
