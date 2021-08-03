T = int(input())
while T > 0:
    N, K = map(int, input().split())
    T = T - 1
    r1 = 1
    r2 = K

    def createList(r1, r2):
        return list(range(r1, r2 + 1))
    L = createList(1, K)
    L.append(N)
    k = K + 1
    while k < N:
        L.append(k)
        k = k + 1
    print(*L)
