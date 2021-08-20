(N, K, M) = list(map(int, input().split()))
A = list(map(int, input().split()))
tt = 0
i = 0
while i < N:
    k1 = -1
    j = 0
    c = 0
    while j < K and i < N:
        if A[i] != 0:
            k1 = i
        c = c + A[i]
        i = i + 1
        j = j + 1
    while c >= M and i < N:
        if A[i] != 0:
            k1 = i
        c = c + A[i] - A[i - K]
        i = i + 1
    if k1 < 0:
        tt = -1
        break
    elif c < M and j == K:
        tt = tt + 1
        i = k1 + K
print(tt)
