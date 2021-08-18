import random
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


def compress(array):
    set_ = set([])
    for i in range(len(array)):
        a, b = array[i]
        set_.add(a)
        set_.add(b)
    memo = {value: index for index, value in enumerate(sorted(list(set_)))}
    max_ = 0
    for i in range(len(array)):
        array[i][0] = memo[array[i][0]]
        array[i][1] = memo[array[i][1]]
        max_ = max(max_, *array[i])
    return max_, array


query = []
for i in range(n):
    x1, y1, x2, y2 = info[i]
    if (x1 % r == 0 or y1 % c == 0) and (x2 % r == 0 or y2 % c == 0):
        pos1, pos2 = solve(x1, y1), solve(x2, y2)
        if pos1 > pos2:
            pos1, pos2 = pos2, pos1
        query.append([pos1, pos2 + 1])

m, query = compress(query)
bit = BIT(m)
for i in range(len(query)):
    begin, end = query[i]
    if bit.get_val(begin) != bit.get_val(end - 1):
        print("NO")
        return
    tmp = random.randrange(0, 10**18)
    bit.add(begin, end, tmp)
print("YES")
