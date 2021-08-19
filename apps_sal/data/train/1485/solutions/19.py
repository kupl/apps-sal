for T in range(int(input())):
    N = int(input())
    P = [0] * N
    Q = [0] * N
    R = [0] * N
    X = N // 2
    for I in range(N):
        P[I] = input()
    for I in range(N):
        for J in range(X):
            if P[I][J] == '1':
                Q[I] += 1
            if P[I][J + X] == '1':
                R[I] += 1
    S = sum(Q) - sum(R)
    Z = {abs(S)}
    for I in range(N):
        if Q[I] != R[I]:
            Z.add(abs(S + 2 * (R[I] - Q[I])))
    print(min(Z))
