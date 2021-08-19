from collections import deque
import heapq
import sys
input = sys.stdin.readline


class SparseTable:
    """区間取得クエリをO(1)で答えるデータ構造をO(NlogN)で構築する
    query(l, r): 区間[l, r)に対するクエリに答える
    """

    def __init__(self, array, n):
        n = len(array)
        self.row_size = n.bit_length()
        self.log_table = [0] * (n + 1)
        for i in range(2, n + 1):
            self.log_table[i] = self.log_table[i // 2] + 1
        self.sparse_table = [[0] * n for _ in range(self.row_size)]
        for i in range(n):
            self.sparse_table[0][i] = array[i]
        for row in range(1, self.row_size):
            for i in range(n - (1 << row) + 1):
                self.sparse_table[row][i] = self._merge(self.sparse_table[row - 1][i], self.sparse_table[row - 1][i + (1 << row - 1)])

    def _merge(self, num1, num2):
        """クエリの内容"""
        return min(num1, num2)

    def query(self, l, r):
        """区間[l, r)に対するクエリに答える"""
        row = self.log_table[r - l]
        return self._merge(self.sparse_table[row][l], self.sparse_table[row][r - (1 << row)])


n = int(input())
p = list(map(int, input().split()))
q = [[0] * (n // 2) for i in range(2)]
for i in range(n):
    q[i % 2][i // 2] = p[i]
ind = {}
for i in range(n):
    ind[p[i]] = i
sp0 = SparseTable(q[0], n // 2)
sp1 = SparseTable(q[1], n // 2)
con = {}
ans = {}
div = 10 ** 6


def solve(l, r):
    q = deque([l * div + r])
    while q:
        pos = q.pop()
        (l, r) = (pos // div, pos % div)
        if l % 2 == 0:
            min1 = sp0.query(l // 2, r // 2)
        else:
            min1 = sp1.query(l // 2, r // 2)
        use_pos1 = ind[min1]
        if (l + 1) % 2 == 0:
            min2 = sp0.query((use_pos1 + 1) // 2, (r + 1) // 2)
        else:
            min2 = sp1.query((use_pos1 + 1) // 2, (r + 1) // 2)
        use_pos2 = ind[min2]
        ans[pos] = min1 * div + min2
        con[pos] = []
        if l != use_pos1:
            con[pos].append(l * div + use_pos1)
            q.append(l * div + use_pos1)
        if use_pos1 + 1 != use_pos2:
            con[pos].append((use_pos1 + 1) * div + use_pos2)
            q.append((use_pos1 + 1) * div + use_pos2)
        if use_pos2 + 1 != r:
            con[pos].append((use_pos2 + 1) * div + r)
            q.append((use_pos2 + 1) * div + r)
    return


solve(0, n)
res = []
q = [(ans[n], n)]
while q:
    (num, i) = heapq.heappop(q)
    (min1, min2) = (num // div, num % div)
    res.append(min1)
    res.append(min2)
    for new_num in con[i]:
        heapq.heappush(q, (ans[new_num], new_num))
print(*res)
