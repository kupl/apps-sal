import heapq as hp
import sys
input = sys.stdin.readline


class SparseTable:

    def __init__(self, N, A):
        self.N = N
        self.logN = N.bit_length()
        self.A = A
        self.table = [[i for i in range(N)]]
        for k in range(self.logN):
            tab = []
            for i in range(self.N - (1 << k + 1) + 1):
                ind1 = self.table[-1][i]
                ind2 = self.table[-1][i + (1 << k)]
                if self.A[ind1] <= self.A[ind2]:
                    tab.append(ind1)
                else:
                    tab.append(ind2)
            self.table.append(tab)

    def query_min(self, l, r):
        k = (r - l).bit_length() - 1
        indl = self.table[k][l]
        indr = self.table[k][r - (1 << k)]
        if self.A[indl] <= self.A[indr]:
            return (self.A[indl], indl)
        return (self.A[indr], indr)


N = int(input())
A = list(map(int, input().split()))


def main():
    SP1 = SparseTable((N + 1) // 2, A[::2])
    SP2 = SparseTable(N // 2, A[1::2])
    ans = []
    q = []
    (v, k) = SP1.query_min(0, N // 2)
    dic = {}
    dic[v] = (k, 0, N // 2, True)
    hp.heappush(q, v)
    for _ in range(N // 2):
        valuea = hp.heappop(q)
        (ka, l, r, is1) = dic[valuea]
        ans.append(str(valuea))
        if is1:
            (valueb, kb) = SP2.query_min(ka, r)
            if ka < kb:
                (m2, nk2) = SP2.query_min(ka, kb)
                hp.heappush(q, m2)
                dic[m2] = (nk2, ka, kb + 1, False)
            if l < ka:
                (m1, nk1) = SP1.query_min(l, ka)
                hp.heappush(q, m1)
                dic[m1] = (nk1, l, ka, True)
            if kb + 1 < r:
                (m3, nk3) = SP1.query_min(kb + 1, r)
                hp.heappush(q, m3)
                dic[m3] = (nk3, kb + 1, r, True)
        else:
            (valueb, kb) = SP1.query_min(ka + 1, r)
            if ka + 1 < kb:
                (m1, nk1) = SP1.query_min(ka + 1, kb)
                hp.heappush(q, m1)
                dic[m1] = (nk1, ka + 1, kb, True)
            if l < ka:
                (m2, nk2) = SP2.query_min(l, ka)
                hp.heappush(q, m2)
                dic[m2] = (nk2, l, ka + 1, False)
            if kb < r - 1:
                (m3, nk3) = SP2.query_min(kb, r - 1)
                hp.heappush(q, m3)
                dic[m3] = (nk3, kb, r, False)
        ans.append(str(valueb))
    print(' '.join(ans))


def __starting_point():
    main()


__starting_point()
