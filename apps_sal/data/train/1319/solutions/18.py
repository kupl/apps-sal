try:
    (N, M) = list(map(int, input().split()))
    L = []
    for i in range(N + M):
        L.append(int(input()))
    l = []
    for i in L:
        if i != -1:
            l.append(i)
        else:
            print(max(l))
            l.remove(max(l))
except:
    pass
