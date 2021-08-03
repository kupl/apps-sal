def main():
    N = int(input())
    D = [int(input()) for i in range(N)]
    C = [1] * N
    T = [0] * N
    DI = {}
    for i in range(len(D)):
        DI[D[i]] = i
    D = sorted(D)
    P = [-1] * N
    while len(D) > 1:
        d = D.pop()
        i = DI[d]
        nd = d - N + C[i] * 2
        if nd in DI:
            ni = DI[nd]
        else:
            print(-1)
            return
        P[i] = ni
        C[ni] += C[i]
        T[ni] += T[i] + C[i]

    if D[0] == T[DI[D[0]]]:
        for i in range(N):
            if P[i] >= 0:
                print(i + 1, P[i] + 1)
    else:
        print(-1)


main()
