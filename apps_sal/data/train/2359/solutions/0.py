(N, K, M) = map(int, input().split())
R = range
T = [[1]]
for i in R(1, N):
    q = K * i
    if i > ~i + N:
        T += [(y := T[-1][:len(T[~i + N])])]
    else:
        T += [(y := (T[-1][:] + [0] * q))]
    p = len(y) - i
    for j in R(p):
        y[j + i] += y[j] % M
    for j in R(p - q):
        y[~j] -= y[~j - i - q] % M
for i in R(N):
    print(sum((T[i][j] * T[~i + N][j] for j in R(len(T[i])))) * -~K % M - 1)
