class Solution:

    def minCostConnectPoints(self, A: List[List[int]]) -> int:
        self.graph = []

        def find(par, i):
            if par[i] == i:
                return i
            return find(par, par[i])

        def union(par, rank, x, y):
            xroot = find(par, x)
            yroot = find(par, y)
            if rank[xroot] < rank[yroot]:
                par[xroot] = yroot
            elif rank[xroot] > rank[yroot]:
                par[yroot] = xroot
            else:
                par[yroot] = xroot
                rank[xroot] += 1

        def kruskal():
            result = []
            i = 0
            e = 0
            self.graph = sorted(edges, key=lambda item: item[2])
            par = []
            rank = []
            for node in range(len(A)):
                par.append(node)
                rank.append(0)
            while e < len(A) - 1:
                (u, v, w) = self.graph[i]
                i = i + 1
                x = find(par, u)
                y = find(par, v)
                if x != y:
                    e = e + 1
                    result.append([u, v, w])
                    union(par, rank, x, y)
            return result
        edge = defaultdict(list)
        edges = []
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                x = abs(A[i][0] - A[j][0])
                y = abs(A[i][1] - A[j][1])
                edges.append([i, j, x + y])
        res = kruskal()
        main = 0
        for i in res:
            main += i[-1]
        return main
