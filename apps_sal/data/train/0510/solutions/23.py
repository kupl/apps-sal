import sys
input = sys.stdin.readline


def solve():
    ordA = ord('a')

    N = int(input())
    Ss = input().rstrip()
    Q = int(input())
    querys = [tuple(input().split()) for _ in range(Q)]

    idEle = 0

    def _binOpe(x, y):
        return x | y

    def makeSegTree(numEle):
        numPow2 = 2 ** (numEle - 1).bit_length()
        data = [idEle] * (2 * numPow2)
        return data, numPow2

    def setInit(As):
        for iST, A in enumerate(As, numPow2):
            data[iST] = A
        for iST in reversed(list(range(1, numPow2))):
            data[iST] = _binOpe(data[2 * iST], data[2 * iST + 1])

    def _update1(iA, A):
        iST = iA + numPow2
        data[iST] = A

    def update(iA, A):
        _update1(iA, A)
        iST = iA + numPow2
        while iST > 1:
            iST >>= 1
            data[iST] = _binOpe(data[2 * iST], data[2 * iST + 1])

    def getValue(iSt, iEn):
        L = iSt + numPow2
        R = iEn + numPow2
        ans = idEle
        while L < R:
            if L & 1:
                ans = _binOpe(ans, data[L])
                L += 1
            if R & 1:
                R -= 1
                ans = _binOpe(ans, data[R])
            L >>= 1
            R >>= 1
        return ans

    data, numPow2 = makeSegTree(N)
    As = [(1 << (ord(S) - ordA)) for S in Ss]
    setInit(As)

    anss = []
    for tp, *vs in querys:
        if tp == '1':
            i, c = vs
            i = int(i)
            update(i - 1, 1 << (ord(c) - ordA))
        else:
            L, R = vs
            L, R = int(L), int(R)
            v = getValue(L - 1, R)
            anss.append(bin(v).count('1'))

    print(('\n'.join(map(str, anss))))


solve()
