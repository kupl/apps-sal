import sys
from operator import itemgetter
mod = 10 ** 9 + 7
inf = 1 << 30


def solve():
    (N, M) = map(int, sys.stdin.readline().split())
    sects = []
    for i in range(N):
        (li, ri) = map(int, sys.stdin.readline().split())
        sects.append((li, ri + 1, ri - li + 1))
    sects.sort(key=itemgetter(2))
    print(N)
    left = 0
    ft = FenwickTree(M + 1)
    for d in range(2, M + 1):
        for j in range(left, N):
            if sects[j][2] >= d:
                left = j
                break
            else:
                ft.add(sects[j][0], 1)
                ft.add(sects[j][1], -1)
        else:
            left = N
        ans = N - left + sum((ft.get_sum(j) for j in range(d, M + 1, d)))
        print(ans)


class FenwickTree:

    def __init__(self, size):
        self.n = size
        self.data = [0] * (size + 1)

    def add(self, i, x):
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get_sum(self, r):
        res = 0
        while r > 0:
            res += self.data[r]
            r -= r & -r
        return res


def __starting_point():
    solve()


__starting_point()
