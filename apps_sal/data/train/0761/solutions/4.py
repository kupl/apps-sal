for tests in range(eval(input())):
    [N, K, M] = list(map(int, input().split()))
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(int, input().split()))
    D = list(map(int, input().split()))
    E = [0] * N
    F = [0] * (K + M)
    for i in range(N):
        E[i] = A[i] - B[i]
    for i in range(K):
        F[i] = C[i]
    for i in range(M):
        F[i + K] = D[i]
    E = sorted(E, reverse=True)
    F = sorted(F, reverse=True)
    k = 0
    for i in range(K + M):
        if E[k] >= F[i]:
            E[k] = E[k] - F[i]
            k = k + 1
    print(sum(E))
