from operator import itemgetter
import sys
input = sys.stdin.readline


class BIT:
    """区間加算、一点取得クエリをそれぞれO(logN)で答えるデータ構造"""

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def _add(self, i, val):
        while i > 0:
            self.bit[i] += val
            i -= i & -i

    def get_val(self, i):
        """i番目の値を求める"""
        i = i + 1
        s = 0
        while i <= self.n:
            s += self.bit[i]
            i += i & -i
        return s

    def add(self, l, r, val):
        """区間[l, r)にvalを加える"""
        self._add(r, val)
        self._add(l, -val)


n, m = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n)]

for i in range(n):
    info[i] = info[i][0], info[i][1], info[i][1] - info[i][0] + 1
info = sorted(info, key=itemgetter(2))

bit = BIT(m + 1)
l_info = 0
ans = n
for d in range(1, m + 1):
    while True:
        if l_info < n and info[l_info][2] < d:
            l, r, _ = info[l_info]
            bit.add(l, r + 1, 1)
            l_info += 1
            ans -= 1
        else:
            break
    cnt = ans
    for i in range(0, m + 1, d):
        cnt += bit.get_val(i)
    print(cnt)
