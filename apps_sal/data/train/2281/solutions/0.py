import sys
from collections import deque


class BIT():
    """区間加算、一点取得クエリをそれぞれO(logN)で応えるデータ構造を構築する
    add: 区間[begin, end)にvalを加える
    get_val: i番目(0-indexed)の値を求める
    """

    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def get_val(self, i):
        i = i + 1
        s = 0
        while i <= self.n:
            s += self.bit[i]
            i += i & -i
        return s

    def _add(self, i, val):
        while i > 0:
            self.bit[i] += val
            i -= i & -i

    def add(self, i, j, val):
        self._add(j, val)
        self._add(i, -val)


input = sys.stdin.readline


def eular_tour(tree: list, root: int):
    """頂点に対するオイラーツアーを行う
    posの部分木に区間[begin[pos], end[pos])が対応する
    """
    n = len(tree)
    res = []
    begin = [-1] * n
    end = [-1] * n
    visited = [False] * n
    visited[root] = True
    q = deque([root])
    while q:
        pos = q.pop()
        res.append(pos)
        end[pos] = len(res)
        if begin[pos] == -1:
            begin[pos] = len(res) - 1
        for next_pos in tree[pos]:
            if visited[next_pos]:
                continue
            else:
                visited[next_pos] = True
                q.append(pos)
                q.append(next_pos)

    return res, begin, end


n, q = map(int, input().split())
init_cost = list(map(int, input().split()))
info = [list(map(int, input().split())) for i in range(n - 1)]
query = [list(map(int, input().split())) for i in range(q)]

tree = [[] for i in range(n)]
for i in range(n - 1):
    a, b = info[i]
    a -= 1
    b -= 1
    tree[a].append(b)
    tree[b].append(a)

res, begin, end = eular_tour(tree, 0)
even_res = []
odd_res = []
for i in range(len(res)):
    if i % 2 == 0:
        even_res.append(res[i])
    else:
        odd_res.append(res[i])

even_bit = BIT(len(even_res))
odd_bit = BIT(len(odd_res))

for i in range(q):
    if query[i][0] == 1:
        _, pos, cost = query[i]
        pos -= 1
        if begin[pos] % 2 == 0:
            even_bit.add(begin[pos] // 2, (end[pos] + 1) // 2, cost)
            odd_bit.add(begin[pos] // 2, end[pos] // 2, -cost)
        else:
            odd_bit.add(begin[pos] // 2, end[pos] // 2, cost)
            even_bit.add((begin[pos] + 1) // 2, end[pos] // 2, -cost)
    else:
        _, pos = query[i]
        pos -= 1
        if begin[pos] % 2 == 0:
            ans = even_bit.get_val(begin[pos] // 2)
        else:
            ans = odd_bit.get_val(begin[pos] // 2)
        print(ans + init_cost[pos])
