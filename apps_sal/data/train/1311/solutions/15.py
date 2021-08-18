from math import ceil
T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    L = []
    for i in range(1, N + 1):
        if i % 2 == 0:
            L.append(-i)
        else:
            L.append(i)
    C = ceil(N / 2)
    if K <= C:
        d = C - K

        c = 0
        for i in range(N - 1, -1, -1):
            if c == d:
                break
            if L[i] > 0:
                L[i] = -(L[i])
                c += 1
    else:
        d = K - C
        c = 0
        for i in range(N - 1, -1, -1):
            if c == d:
                break
            if L[i] < 0:
                L[i] = abs(L[i])
                c += 1
    print(*L)
