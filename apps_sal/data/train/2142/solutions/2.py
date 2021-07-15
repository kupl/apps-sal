n = int(input())
if n > 1:
    p = [0] * n
    r = format(n - 1, 'b')[:: -1]
    l = len(r) - 1
    for i in range(n):
        t = list(map(int, input().split()))
        t.pop(i)
        s = 0
        for j in range(l):
            if r[j]  == '1': s |= t.pop()
            t = [t[k] | t[k + 1] for k in range(0, len(t), 2)]
        p[i] = s | t[0]
    print(' '.join(map(str, p)))
else: print(0)
