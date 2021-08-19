class SegTree:
    def __init__(self, init_val, ide_ele, segfunc):
        self.n = len(init_val)
        self.num = 2**(self.n - 1).bit_length()
        self.ide_ele = ide_ele
        self.seg = [self.ide_ele] * 2 * self.num
        self.segfunc = segfunc

        # set_val
        for i in range(self.n):
            self.seg[i + self.num - 1] = init_val[i]
        # built
        for i in range(self.num - 2, -1, -1):
            self.seg[i] = segfunc(self.seg[2 * i + 1], self.seg[2 * i + 2])

    def update(self, k, x):
        k += self.num - 1
        self.seg[k] = x
        while k + 1:
            k = (k - 1) // 2
            self.seg[k] = self.segfunc(self.seg[k * 2 + 1], self.seg[k * 2 + 2])

    def query(self, p, q):
        if q <= p:
            return self.ide_ele
        p += self.num - 1
        q += self.num - 2
        res = self.ide_ele
        while q - p > 1:
            if p & 1 == 0:
                res = self.segfunc(res, self.seg[p])
            if q & 1 == 1:
                res = self.segfunc(res, self.seg[q])
                q -= 1
            p = p // 2
            q = (q - 1) // 2
        if p == q:
            res = self.segfunc(res, self.seg[p])
        else:
            res = self.segfunc(self.segfunc(res, self.seg[p]), self.seg[q])
        return res


def main():
    import sys
    input = sys.stdin.readline

    N = int(input())
    P = list(map(int, input().split()))
    Even = []
    Odd = []
    D = {}
    for i in range(N // 2):
        e = P[2 * i]
        o = P[2 * i + 1]
        D[e] = i
        D[o] = i
        Even.append(e)
        Odd.append(o)

    E_Seg = SegTree(Even, float("inf"), min)
    O_Seg = SegTree(Odd, float("inf"), min)

    import heapq
    heap = []
    # heapq.heappush(heap, item)
    # heapq.heappop(heap)

    def BFS(H):
        L = H[0]
        R = H[1]
        if R <= L:
            return -1, -1, -1, -1, -1
        if L % 2 == 0:
            l = L // 2
            r = R // 2
            mini = E_Seg.query(l, r + 1)
            d_mini = D[mini]
            mini_b = O_Seg.query(d_mini, r + 1)
            d_mini_b = D[mini_b]

            leftH = (L, 2 * d_mini - 1)
            centH = (2 * d_mini + 1, 2 * d_mini_b)
            rightH = (2 * d_mini_b + 2, R)
            return mini, mini_b, leftH, centH, rightH
        else:
            l = L // 2
            r = R // 2
            mini = O_Seg.query(l, r)
            d_mini = D[mini]
            mini_b = E_Seg.query(d_mini + 1, r + 1)
            d_mini_b = D[mini_b]

            leftH = (L, 2 * d_mini)
            centH = (2 * d_mini + 2, 2 * d_mini_b - 1)
            rightH = (2 * d_mini_b + 1, R)
            return mini, mini_b, leftH, centH, rightH

    H = (0, N - 1)
    m1, m2, LH, CH, RH = BFS(H)
    # print(m1,m2)
    heapq.heappush(heap, [m1, m2, LH, CH, RH])
    Q = []
    while heap != []:
        m1, m2, LH, CH, RH = heapq.heappop(heap)
        Q += [m1, m2]

        m1L, m2L, LHL, CHL, RHL = BFS(LH)
        if m1L != -1:
            heapq.heappush(heap, [m1L, m2L, LHL, CHL, RHL])

        m1C, m2C, LHC, CHC, RHC = BFS(CH)
        if m1C != -1:
            heapq.heappush(heap, [m1C, m2C, LHC, CHC, RHC])

        m1R, m2R, LHR, CHR, RHR = BFS(RH)
        if m1R != -1:
            heapq.heappush(heap, [m1R, m2R, LHR, CHR, RHR])
    print(*Q)


main()
