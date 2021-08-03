for _ in range(int(input())):
    N, M = list(map(int, input().split()))
    A = []
    B = [['0' for x in range(M)] for x in range(N)]
    for __ in range(N):
        A.append(input().split())

    D = {}
    for i in range(N):
        for j in range(M):
            D[int(A[i][j])] = (i, j)

    for k in range(1, N * M + 1):
        i, j = D[k]
        B[i][j] = '1'
        for p in range(i + 1, N):
            diff = p - i
            for q in range(j - diff, j + diff + 1):
                if q >= 0 and q < M:
                    B[p][q] = '0'

    for i in B:
        for j in i:
            print(j, end='')
        print()
