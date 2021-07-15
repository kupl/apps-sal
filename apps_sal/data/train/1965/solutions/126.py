class DisjointSet:
    def __init__(self, elements):
        self.parent = [i for i in range(elements)]
        self.size = [1] * elements
    def find(self, value):
        if self.parent[value] != value:
            self.parent[value] = self.find(self.parent[value])
        return self.parent[value]
    def union(self, value1, value2):
        parent1, parent2 = self.find(value1), self.find(value2)
        if parent1 == parent2:
            return True
        if self.size[parent1] > self.size[parent2]:
            self.parent[parent2] = parent1
            self.size[parent1] += self.size[parent2]
        else:
            self.parent[parent1] = parent2
            self.size[parent2] += self.size[parent1]
        return False
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        graph = [list() for i in range(n + 1)]
        for t, u, v in edges:
            graph[u].append([v, t])
            graph[v].append([u, t])
        def dfs(source, ty):
            nonlocal cnt
            cnt += 1
            vis[source] = 1
            for child, typer in graph[source]:
                if typer in [ty, 3] and not vis[child]:
                    dfs(child, ty)
        cnt = 0
        vis = [0] * (n + 1)
        dfs(1, 1)
        if cnt != n:
            return -1
        vis = [0] * (n + 1)
        cnt = 0
        dfs(1, 2)
        if cnt != n:
            return -1
        answer = 0
        dsu1, dsu2 = DisjointSet(n + 1), DisjointSet(n + 1)
        for t, u, v in edges:
            if t == 3:
                dsu1.union(u, v)
                if dsu2.union(u, v):
                    answer += 1
        for t, u, v in edges:
            if t == 1:
                if dsu1.union(u, v):
                    answer += 1
            if t == 2:
                if dsu2.union(u, v):
                    answer += 1
        return answer

