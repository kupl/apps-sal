N, M, P = list(map(int, input().split()))
A = [dict() for _ in range(N)]
for _ in range(P):
    i, j = list(map(int, input().split()))
    i -= 1
    j -= 1
    if j not in A[i]:
        A[i][j] = j + 1
    else:
        A[i][j] += 1


def solve(A, i):
    for (k, v) in A[i].items():
        if k == M - 1:
            continue
        if k + 1 in A[i]:
            c = A[i][k + 1]
        else:
            c = k + 1
        if A[i][k] > c:
            return -1
    y = A[i][M - 1] if M - 1 in A[i] else M - 1
    x = A[i][0] if 0 in A[i] else 0
    return y - x


for i in range(N):
    print(solve(A, i))
