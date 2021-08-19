class UnionFind:

    def __init__(self):
        self.reps = {}
        self.ranks = {}

    def makeset(self, x):
        self.reps[x] = x
        self.ranks[x] = 0

    def find(self, x):
        if self.reps[x] != x:
            self.reps[x] = self.find(self.reps[x])
        return self.reps[x]

    def union(self, x, y):
        rep_x = self.find(x)
        rep_y = self.find(y)
        if self.ranks[rep_x] > self.ranks[rep_y]:
            self.reps[rep_y] = rep_x
        elif self.ranks[rep_x] == self.ranks[rep_y]:
            self.reps[rep_y] = rep_x
            self.ranks[rep_x] += 1
        else:
            self.reps[rep_x] = rep_y


class Solution:

    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        unionfind = UnionFind()
        for i in range(N):
            unionfind.makeset(i + 1)
        graph = {}
        for (u, v) in dislikes:
            graph.setdefault(u, [])
            graph[u].append(v)
            graph.setdefault(v, [])
            graph[v].append(u)
        for person in graph:
            for enemy in graph[person]:
                rep_u = unionfind.find(person)
                rep_v = unionfind.find(enemy)
                if rep_u != rep_v:
                    unionfind.union(graph[person][0], enemy)
                else:
                    return False
        return True
