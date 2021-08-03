def era(n):

    l = [True for i in range(0, n + 1)]
    l[0] = l[1] = False
    for i in range(2, n + 1):
        if l[i]:
            for j in range(i * i, n + 1, i):
                l[j] = False
    for i, _ in enumerate(l):
        if _:
            yield i


def goldbach(n):
    res = []
    p = list(era(n))
    for x in p:
        if n - x in p:
            if n - x < x:
                return res
            res.append([x, n - x])
    return res
