from heapq import *
import sys

sys.setrecursionlimit(10 ** 6)
def int1(x): return int(x) - 1
def p2D(x): return print(*x, sep="\n")
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]


class SparseTable:
    def __init__(self, aa):
        inf = 10 ** 16
        w = len(aa)
        h = w.bit_length()
        table = [aa] * 2 + [[inf] * w for _ in range(h - 2)]
        tablei1 = table[0]
        for i in range(2, h):
            tablei = table[i]
            shift = 1 << (i - 1)
            for j in range(w):
                rj = j + shift
                if rj >= w:
                    break
                tablei[j] = min(tablei1[j], tablei1[rj])
            tablei1 = tablei
        self.table = table

    def min(self, l, r):
        if (r - l) % 2:
            r += 1
        i = (r - l).bit_length() - 1
        tablei = self.table[i]
        Lmin = tablei[l]
        Rmin = tablei[r - (1 << i)]
        if Lmin < Rmin:
            Rmin = Lmin
        return Rmin


def main():
    n = int(input())
    pp = LI()
    st = SparseTable(pp)
    ptoi = [0] + [i for i, p in sorted(enumerate(pp), key=lambda x: x[1])]
    hp = []
    heappush(hp, [st.min(0, n), 0, n])
    ans = []
    for _ in range(n // 2):
        x, l, r = heappop(hp)
        if l + 2 == r:
            ans += [pp[l], pp[l + 1]]
            continue
        xi = ptoi[x]
        y = st.min(xi + 1, r)
        yi = ptoi[y]
        if xi > l:
            heappush(hp, [st.min(l, xi), l, xi])
        if xi + 1 < yi:
            heappush(hp, [st.min(xi + 1, yi), xi + 1, yi])
        if yi < r - 1:
            heappush(hp, [st.min(yi + 1, r), yi + 1, r])
        ans += [x, y]
    print(*ans)


main()
