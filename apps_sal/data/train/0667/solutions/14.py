for _ in range(int(input())):
    (N, D) = map(int, input().split())
    R = list(map(int, input().split()))
    Cur = D
    for i in range(N - 1, -1, -1):
        if i == N - 1:
            T = Cur // R[i]
            R[i] = R[i] * T
            Cur = R[i]
        else:
            T = Cur // R[i]
            R[i] = R[i] * T
            Cur = R[i]
    print(Cur)
