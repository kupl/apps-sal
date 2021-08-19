for T in range(0, int(input())):
    if T <= 10:
        N = int(input())
        if N <= 100:
            L1 = [[0 for i in range(0, N)] for j in range(0, N)]
            c = 1
            for i in range(0, N):
                a = 0
                for j in range(i, -1, -1):
                    L1[a][j] = c
                    c += 1
                    a += 1
            for x in range(1, N):
                k = x
                for y in range(N - x):
                    L1[k][N - y - 1] = c
                    c += 1
                    k += 1
            for mat in L1:
                print(*mat)
