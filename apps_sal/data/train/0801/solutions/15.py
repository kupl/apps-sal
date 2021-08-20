for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    f1 = dict()
    f2 = dict()
    mn = min(min(a), min(b))
    for d in a:
        if d in f1:
            l = f1[d]
            f1[d] = l + 1
        else:
            f1[d] = 1
    for d in b:
        if d in f2:
            l = f2[d]
            f2[d] = l + 1
        else:
            f2[d] = 1
    tot = dict(f1)
    for d in f2:
        if d in tot:
            l = tot[d]
            tot[d] = l + f2[d]
        else:
            tot[d] = f2[d]
    flg = False
    for d in tot.values():
        if d % 2 != 0:
            flg = True
            break
    if flg:
        print('-1')
        continue
    x = []
    for d in tot:
        t = tot.get(d, 0) // 2
        l = f1.get(d, 0)
        r = f2.get(d, 0)
        if l > t:
            k = l - t
            for i in range(k):
                x.append(d)
        if r > t:
            k = r - t
            for i in range(k):
                x.append(d)
    for i in range(len(x)):
        if x[i] > 2 * mn:
            x[i] = 2 * mn
    x.sort()
    ln = len(x) // 2
    y = x[:ln]
    ans = sum(y)
    print(ans)
