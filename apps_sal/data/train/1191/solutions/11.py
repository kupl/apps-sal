for i in range(int(input())):
    n, q = map(int, input().split())
    nn = []
    qq = []
    for j in range(n):
        nn.append(input())
    for j in range(q):
        qq.append(input())
    for j in qq:
        l3 = []
        for k in nn:
            if len(j) < 4:
                a, b = 1, 1
            elif len(j) < 20:
                a, b = 2, 1
            elif len(j) < 40:
                a, b = 3, 2
            elif len(j) <= 100:
                a, b = 5, 4
            m = 0
            for l in range(0, len(j), b):
                try:
                    d = j[l:l + a]
                    m += k.count(j[l:l + a])
                except IndexError:
                    break
            l3.append(m)
        print(nn[l3.index(max(l3))])
