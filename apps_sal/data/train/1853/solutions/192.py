class Solution:

    def dfs(self, q, D, V, k):
        Q = [q]
        V[q] = 0
        while Q:
            T = []
            for nd in Q:
                W = V[nd]
                for (n, w) in D[nd]:
                    cl = W + w
                    cr = V[n]
                    if cl < cr and cl <= k:
                        V[n] = cl
                        T.append(n)
            Q = T
        return {a: b for (a, b) in list(V.items()) if b != sys.maxsize}

    def findTheCity(self, N: int, E: List[List[int]], k: int) -> int:
        D = collections.defaultdict(list)
        for (f, t, w) in E:
            D[f].append((t, w))
            D[t].append((f, w))
        R = dict()
        mn = sys.maxsize
        for q in range(N):
            V = self.dfs(q, D, collections.defaultdict(lambda: sys.maxsize), k)
            R[q] = V
            if mn > len(V):
                mn = len(V)
        R = {a: b for (a, b) in list(R.items()) if len(b) == mn}
        return max(R.keys())
