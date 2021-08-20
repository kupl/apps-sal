for _ in range(int(input())):
    (N, M) = list(map(int, input().split()))
    A = []
    B = [['1' for x in range(M)] for x in range(N)]
    C = [['1' for x in range(M)] for x in range(N)]
    for __ in range(N):
        A.append(list(map(int, input().split())))
    B[0] = A[0].copy()
    for i in range(1, N):
        p = i - 1
        for j in range(0, M):
            B[i][j] = A[p][j]
            B[i][j] = max(B[i][j], A[i][j])
            if j >= 1:
                B[i][j] = max(B[i][j], B[p][j - 1])
            if j <= M - 2:
                B[i][j] = max(B[i][j], B[p][j + 1])
    C[0] = [1] * M
    for i in range(1, N):
        for j in range(0, M):
            if B[i][j] > A[i][j]:
                C[i][j] = 0
    for i in range(0, N):
        for j in range(0, M):
            print(C[i][j], end='')
        print()
