

try:
    import psyco
    psyco.full()
except ImportError:
    pass


def main(N, M, P, tab):
    """Evolved solution"""
    dtab = dict()
    for ii, jj in tab:
        i, j = ii - 1, jj - 1
        if i in dtab:
            dtab[i].append(j)
        else:
            dtab[i] = [j]

    for i in range(N):
        sol = M - 1
        if i in dtab:
            line = sorted(dtab[i])
            sol += line.count(M - 1) - line.count(0)
            prev = -1
            for k in line:
                if k > prev and k < (M - 1):
                    inc_k = line.count(k)
                    inc_kp = line.count(k + 1)
                    if inc_k > (inc_kp + 1):
                        sol = -1
                        break
                    prev = k

        print(sol)


def __starting_point():
    N, M, P = list(map(int, input().split()))
    tab = [list(map(int, input().split())) for _ in range(P)]
    main(N, M, P, tab)


__starting_point()
