for _ in range(int(input())):
    (n, k) = list(map(int, input().split()))
    aux = {}
    for i in range(n):
        (s, f, p) = list(map(int, input().split()))
        if p not in aux:
            aux[p] = []
            aux[p].append([s, f])
        else:
            aux[p].append([s, f])
    tot = 0
    for i in aux:
        if len(aux[i]) > 1:
            aux[i].sort(key=lambda x: x[1])
            t_1 = 0
            for j in range(len(aux[i])):
                if aux[i][j][0] >= t_1:
                    t_1 = aux[i][j][1]
                    tot += 1
        else:
            tot += 1
    print(tot)
