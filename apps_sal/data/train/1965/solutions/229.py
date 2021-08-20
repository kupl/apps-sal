import collections
import sys
sys.setrecursionlimit(1000000)


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        to = collections.defaultdict(list)
        for (t, a, b) in edges:
            to[a - 1].append((b - 1, t - 1))
            to[b - 1].append((a - 1, t - 1))

        def is_connected(etype=0):
            remain = [1] * n

            def dfs(n=0):
                if remain[n] == 0:
                    return
                remain[n] = 0
                for (nn, t) in to[n]:
                    if t == etype or t == 2:
                        dfs(nn)
            dfs()
            return len([1 for r in remain if r == 1]) == 0
        if not is_connected(0):
            return -1
        if not is_connected(1):
            return -1
        ids = [i for i in range(n)]

        def find(i):
            if i == ids[i]:
                return i
            ni = find(ids[i])
            ids[i] = ni
            return ni

        def union(i, j):
            i = find(i)
            j = find(j)
            if i == j:
                return False
            ids[j] = i
            return True
        e = 0
        for (t, a, b) in edges:
            if t == 3:
                if union(a - 1, b - 1):
                    e += 1
        ids2 = list(ids)
        for (t, a, b) in edges:
            if t == 1:
                if union(a - 1, b - 1):
                    e += 1
        ids = ids2
        for (t, a, b) in edges:
            if t == 2:
                if union(a - 1, b - 1):
                    e += 1
        return len(edges) - e
