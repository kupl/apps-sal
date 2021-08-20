class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A = [i for i in range(n)]

        def find(u):
            if A[u] != u:
                A[u] = find(A[u])
            return A[u]

        def union(u, v):
            (pu, pv) = (find(u), find(v))
            if pu == pv:
                return False
            A[max(pu, pv)] = min(pu, pv)
            return True
        edges = sorted(edges, reverse=True)
        i = 0
        m = len(edges)
        res = 0
        while i < m:
            cur = edges[i]
            if cur[0] == 3:
                if union(cur[1] - 1, cur[2] - 1) == False:
                    res += 1
            else:
                break
            i += 1
        origin_A = deepcopy(A)
        while i < m:
            cur = edges[i]
            if cur[0] == 2:
                if union(cur[1] - 1, cur[2] - 1) == False:
                    res += 1
            else:
                break
            i += 1
        for j in range(1, n):
            p = find(j)
            if p != 0:
                return -1
        A = origin_A
        while i < m:
            cur = edges[i]
            if cur[0] == 1:
                if union(cur[1] - 1, cur[2] - 1) == False:
                    res += 1
            else:
                break
            i += 1
        for j in range(1, n):
            p = find(j)
            if p != 0:
                return -1
        return res
