class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:

        def method1(dislikes):

            class UF:

                def __init__(self, size):
                    self.p = list(range(size))

                def find(self, x):
                    if x != self.p[x]:
                        self.p[x] = self.find(self.p[x])
                    return self.p[x]

                def union(self, x, y):
                    self.p[self.find(x)] = self.find(y)

                def find_all(self):
                    for i in range(len(self.p)):
                        self.find(i)
            if N < 2 or not dislikes:
                return True
            dislikes = set(map(tuple, dislikes))
            uf = UF(N)
            for i in range(1, N + 1):
                for j in range(i + 1, N + 1):
                    if (i, j) not in dislikes and (j, i) not in dislikes:
                        uf.union(i - 1, j - 1)
            return len(set(uf.p)) == 2

        def method2():
            RED = 0
            BLUE = 1
            graph = collections.defaultdict(list)
            for (u, v) in dislikes:
                graph[u].append(v)
                graph[v].append(u)
            color = {}

            def dfs(node, c):
                if node in color:
                    return color[node] == c
                color[node] = c
                c = BLUE if c == RED else RED
                return all((dfs(nei, c) for nei in graph[node]))
            return all((dfs(node, RED) for node in range(1, N + 1) if node not in color))
        return method2()
