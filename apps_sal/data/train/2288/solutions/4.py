def main():
    import sys
    from operator import itemgetter
    input = sys.stdin.readline

    X = int(input())
    K = int(input())
    R = list(map(int, input().split()))
    Q = []
    for r in R:
        Q.append((r, -1))
    q = int(input())
    for _ in range(q):
        t, a = list(map(int, input().split()))
        Q.append((t, a))
    Q.sort(key=itemgetter(0))

    #print(Q)
    prev = 0
    m = 0
    M = X
    flg = -1
    R_cs = 0
    for t, a in Q:
        if a < 0:
            r = t - prev
            R_cs -= r * flg
            if flg == -1:
                m = max(0, m-r)
                M = max(0, M-r)
                flg = 1
            else:
                m = min(X, m+r)
                M = min(X, M+r)
                flg = -1
            prev = t
        else:
            if m == M:
                if flg == 1:
                    print((min(X, m + t - prev)))
                else:
                    print((max(0, m - t + prev)))
            else:
                am = m + R_cs
                aM = M + R_cs
                #print('am', am, 'aM', aM, m, M)
                if a <= am:
                    if flg == 1:
                        print((min(X, m + t - prev)))
                    else:
                        print((max(0, m - t + prev)))
                elif a >= aM:
                    if flg == 1:
                        print((min(X, M + t - prev)))
                    else:
                        print((max(0, M - t + prev)))
                else:
                    if flg == 1:
                        print((min(X, m + (a - am) + t - prev)))
                    else:
                        print((max(0, m + (a - am) - t + prev)))


def __starting_point():
    main()

__starting_point()
