class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        """always keep type 3 if possible"""
        edges123 = [collections.defaultdict(list) for _ in range(3)]
        for (t, a, b) in edges:
            edges123[t - 1][a - 1].append(b - 1)
        self.res = 0
        Parents = [[i for i in range(n)] for _ in range(2)]
        selectedEdges = [0, 0]

        def FindRoot(n, t):
            if Parents[t][n] != n:
                Parents[t][n] = FindRoot(Parents[t][n], t)
            return Parents[t][n]

        def Uni(x, y, t):
            (rx, ry) = (FindRoot(x, t), FindRoot(y, t))
            if rx == ry:
                return 0
            else:
                Parents[t][rx] = y
                return 1

        def connect(thetype):
            mytypes = [thetype] if thetype < 2 else [0, 1]
            for node in range(n):
                for neighbor in edges123[thetype][node]:
                    if all((Uni(node, neighbor, t) for t in mytypes)):
                        for t in mytypes:
                            selectedEdges[t] += 1
                    else:
                        self.res += 1
        connect(2)
        connect(0)
        connect(1)
        return self.res if all((selectedEdges[t] == n - 1 for t in [0, 1])) else -1
