T = int(input())
for i in range(T):
    N = int(input())
    L = list(map(int, input().split()))
    M = list(range(1, N + 1))
    Z = [0] * N
    L, M = (list(t) for t in zip(*sorted(zip(L, M))))
    cout = (N + 1) // 2
    mybool = True
    for i in range(N):
        Z[i] = L[(i + cout) % N]
        if (Z[i] == L[i]):
            print("No")
            mybool = False
            break
    if mybool:
        print("Yes")
        M, Z = (list(t) for t in zip(*sorted(zip(M, Z))))
        for i in range(N):
            print(Z[i], end=" ")
        print()
