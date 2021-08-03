T = int(input())
for i in range(T):
    B, G = list(map(int, input().split()))
    l = []
    for j in range(B):
        m = list(input())
        l.append(m)
    d = 0
    for k in range(G):
        c = 0
        for n in range(B):
            if l[n][k] == '1':
                c += 1
        if c > 1:
            d += ((c * (c - 1)) // 2)
    print(d)
