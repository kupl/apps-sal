import sys
def input(): return sys.stdin.readline().rstrip()


N, M = list(map(int, input().split()))
D = [{} for _ in range(N)]
for _ in range(M):
    a, b = list(map(int, input().split()))
    a -= 1
    b -= 1
    D[a][b] = 1
    D[b][a] = 1

L = [i - 1 for i in range(N)]
R = [i + 1 for i in range(N)]

F = [0] * N
for i in range(N):
    if F[i]:
        continue
    f = 1
    while f:
        f = 0
        j = R[i]
        while j < N:
            if j in D[i]:
                j = R[j]
                continue
            F[j] = 1
            A = [a for a in D[i] if a not in D[j]]
            if A:
                f = 1
            for a in A:
                if a in D[i]:
                    del D[i][a]
                if i in D[a]:
                    del D[a][i]
            A = [a for a in D[j] if a not in D[i]]
            if A:
                f = 1
            for a in A:
                if a in D[j]:
                    del D[j][a]
                if j in D[a]:
                    del D[a][j]

            if R[j] < N:
                L[R[j]] = L[j]
            if L[j] >= 0:
                R[L[j]] = R[j]
            j = R[j]

print(N - sum(F) - 1)
