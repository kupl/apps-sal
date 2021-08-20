v = []
(n, k) = map(int, input().split())
s = 0
v = [int(x) for x in input().split()]
s = sum(v)
w = []
if s % k != 0:
    print('No')
else:
    ss = s // k
    i = 0
    m = 0
    sm = 0
    while i < n:
        m = 0
        sm = 0
        while i < n and sm < ss:
            sm += v[i]
            m += 1
            i += 1
        if sm > ss:
            print('No')
            break
        else:
            w.append(m)
    else:
        print('Yes')
        for i in range(len(w)):
            print(w[i], end=' ')
