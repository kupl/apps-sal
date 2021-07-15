import sys
input = sys.stdin.readline

def solve():
    def makeBIT(numEle):
        numPow2 = 2 ** (numEle-1).bit_length()
        data = [0] * (numPow2+1)
        return data, numPow2
    def addValue(iA, A):
        iB = iA + 1
        while iB > 0:
            data[iB] += A
            iB -= iB & -iB
    def getValue(iA):
        iB = iA + 1
        ans = 0
        while iB <= numPow2:
            ans += data[iB]
            iB += iB & -iB
        return ans
    def addRangeValue(iFr, iTo, A):
        addValue(iTo, A)
        if iFr > 0:
            addValue(iFr-1, -A)

    N, M = list(map(int, input().split()))
    LRss = [[] for _ in range(M+1)]
    for _ in range(N):
        L, R = list(map(int, input().split()))
        LRss[R-L+1].append((L, R))

    data, numPow2 = makeBIT(M+1)

    anss = []
    numOK = N
    for d in range(1, M+1):
        ans = numOK
        for i in range(d, M+1, d):
            ans += getValue(i)
        anss.append(ans)
        numOK -= len(LRss[d])
        for L, R in LRss[d]:
            addRangeValue(L, R, 1)

    print(('\n'.join(map(str, anss))))


solve()

