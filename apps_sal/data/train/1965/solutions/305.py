class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(x):
            if x != graph[x]:
                graph[x] = find(graph[x])
            return graph[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px != py:
                if size[px] > size[py]:
                    graph[py] = px
                else:
                    graph[px] = py

                return 1
            return 0

        graph = [i for i in range(n + 1)]
        size = [1] * (n + 1)
        res = alice = bob = 0
        for t, i, j in edges:
            if t == 3:
                if union(i, j):
                    alice += 1
                    bob += 1
                else:
                    res += 1

        tmpG = graph[:]
        for t, i, j in edges:
            if t == 1:
                if union(i, j):
                    alice += 1
                else:
                    res += 1

        graph = tmpG

        for t, i, j in edges:
            if t == 2:
                if union(i, j):
                    bob += 1
                else:
                    res += 1

        return res if alice == bob == n - 1 else -1
