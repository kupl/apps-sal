def nCk(N, K):
    nn = N
    klim = min(K, N - K) + 1
    res = 1
    for kk in range(1, klim):
        res *= nn
        res /= kk
        nn -= 1
    return res


def doTest():
    CC = input()
    CCT = CC.split()
    S = int(CCT[0])
    N = int(CCT[1])
    M = int(CCT[2])
    K = int(CCT[3])
    den = nCk(S - 1, N - 1)
    klim = min(M, N)
    num = 0
    for kk in range(K, klim):
        if ((S - M) < (N - kk - 1)):
            continue
        num += nCk(M - 1, kk) * nCk(S - M, N - kk - 1)

    ans = num / float(den)
    print("%.9f" % ans)


T = int(input())
for tt in range(0, T):
    doTest()
