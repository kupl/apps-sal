import operator
for _ in range(0, int(input())):
    [a, b, c] = list(map(int, input().strip().split()))
    x1 = list(map(int, input().strip().split()))
    x2 = list(map(int, input().strip().split()))
    y1 = list(map(int, input().strip().split()))
    z1 = list(map(int, input().strip().split()))
    x = list(map(operator.sub, x1, x2))
    x.sort()
    z = y1 + z1
    z.sort()
    tot = 0
    for p in x:
        minq = 1000000
        pos = -1
        ctrpos = 0
        for q in z:
            if(q > p):
                break
            if (p - q) < minq:
                minq = p - q
                pos = ctrpos
            ctrpos += 1
        if pos != -1:
            tot += minq
            del z[pos]
        else:
            tot += p
    print(tot)
