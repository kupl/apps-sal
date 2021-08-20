def getdiv(m):
    i = 1
    res = []
    while i * i <= m:
        if m % i == 0:
            res.append(i)
            if m // i != i:
                res.append(m // i)
        i += 1
    return res


test = int(input())
for _ in range(test):
    (a, m) = map(int, input().split())
    div = getdiv(m)
    res = []
    for i in div:
        n = (m - i) / a
        if n >= i and n % 1 == 0 and (n % i == 0):
            res.append(int(n))
    res.sort()
    print(len(res))
    for i in res:
        print(i, end=' ')
    print('')
