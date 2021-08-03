from collections import deque
import sys
input = sys.stdin.readline


class BIT():
    """区間加算、一点取得クエリをそれぞれO(logN)で答える
    add: 区間[l, r)にvalを加える
    get_val: i番目の値を求める
    i, l, rは0-indexed
    """

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


r, c, n = map(int, input().split())
info = [list(map(int, input().split())) for i in range(n)]


def solve(x1, y1):
    if y1 == 0:
        return x1
    if x1 == r:
        return r + y1
    if y1 == c:
        return r + c + (r - x1)
    if x1 == 0:
        return r + c + r + (c - y1)


li = []
for i in range(n):
    x1, y1, x2, y2 = info[i]
    if (x1 % r == 0 or y1 % c == 0) and (x2 % r == 0 or y2 % c == 0):
        pos1, pos2 = solve(x1, y1), solve(x2, y2)
        li.append((pos1, i))
        li.append((pos2, i))

li = sorted(li)
q = deque([])
for i in range(len(li)):
    _, j = li[i]
    if q and q[-1] == j:
        q.pop()
    else:
        q.append(j)
if q:
    print("NO")
else:
    print("YES")
