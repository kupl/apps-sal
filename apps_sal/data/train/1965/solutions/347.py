import copy


class DJ_DS():
    def __init__(self, n):
        self.n = n
        self.parent = [i for i in range(n)]
        self.rank = [0 for i in range(n)]
        self.nb_edges = 0

    def find_parent(self, i):  # faster with path compression
        while self.parent[i] != i:
            i = self.parent[i]
        return i

    def union(self, i, j):
        p_i = self.find_parent(i)
        p_j = self.find_parent(j)

        if p_i != p_j:
            self.nb_edges += 1
            if self.rank[p_i] < self.rank[p_j]:
                self.parent[p_i] = p_j
            else:
                self.parent[p_j] = p_i
                if self.rank[p_i] == self.rank[p_j]:
                    self.rank[p_i] += 1

    def perform_merge(self, edges):
        for [u, v] in edges:
            self.union(u, v)


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        nb_edges = len(edges)
        # list of edges of each color individually
        type1, type2, type3 = [], [], []
        for [t, u, v] in edges:
            if t == 1:
                type1.append([u - 1, v - 1])
            elif t == 2:
                type2.append([u - 1, v - 1])
            else:
                type3.append([u - 1, v - 1])

        # Count nb_edges with type 3 only in max forest
        dj_3 = DJ_DS(n)
        dj_3.perform_merge(type3)
        sol_3 = dj_3.nb_edges
        dj_1 = copy.deepcopy(dj_3)
        dj_2 = copy.deepcopy(dj_3)

        # From type 3 forest add edges from type 1 to see if spanning tree, if not return -1
        dj_1.perform_merge(type1)
        if dj_1.nb_edges < n - 1:
            return -1

        # From type 3 forest add edges from type 2 to see if spanning tree, if not return -1
        dj_2.perform_merge(type2)
        if dj_2.nb_edges < n - 1:
            return -1

        return (nb_edges - (sol_3 + 2 * (n - 1 - sol_3)))
