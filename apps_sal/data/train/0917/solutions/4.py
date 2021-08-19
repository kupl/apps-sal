for _ in range(int(input())):
    (n, k) = map(int, input().split())
    l = list(map(int, input().split()))
    aux = []
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            aux.append(abs(l[i] + l[j] - k))
    m = min(aux)
    t_1 = aux.count(m)
    print(m, t_1)
