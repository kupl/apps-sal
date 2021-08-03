from collections import defaultdict


class Solution:
    def shortestPath(self, A: List[List[int]], k: int) -> int:
        dic = defaultdict(list)
        nbs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(A), len(A[0])
        st = [(0, 0, 0)]
        target = m * n - 1
        if target == 0:
            return 0
        while st:
            t = []
            for a, b, c in st:
                x, y = a // n, a % n
                for i, j in nbs:
                    nx, ny = x + i, y + j
                    if 0 <= nx < m and 0 <= ny < n:
                        p = nx * n + ny
                        cost = c + 1 if A[nx][ny] else c
                        if p == target and cost <= k:
                            return b + 1
                        if p not in dic or cost < dic[p][-1][-1]:
                            dic[p].append([b + 1, cost])
                            t.append((p, b + 1, cost))
            st = t
        return -1
