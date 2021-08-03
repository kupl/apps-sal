P, S = list(map(int, (input().split(" "))))
d = []
for p in range(0, P):
    ST = list(map(int, input().split(" ")))
    N = list(map(int, input().split(" ")))
    c = 0
    L = sorted(list(zip(ST, N)))
    for i in range(0, S - 1):
        if(L[i][1] > L[i + 1][1]):
            c = c + 1
    dd = ()
    dd = (c, p + 1)
    d.append(dd)
d = sorted(d)
for i in range(0, P):
    print(d[i][1])
