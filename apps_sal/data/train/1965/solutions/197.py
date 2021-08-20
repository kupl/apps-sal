class UnionFind:

    def __init__(self, n):
        self.roots = [i for i in range(n)]

    def union(self, index1, index2):
        root1 = self.find(index1)
        root2 = self.find(index2)
        if root1 < root2:
            self.roots[root2] = root1
            return 1
        elif root1 > root2:
            self.roots[root1] = root2
            return 1
        return 0

    def find(self, index):
        if self.roots[index] != index:
            self.roots[index] = self.find(self.roots[index])
        return self.roots[index]


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: -x[0])
        uf1 = UnionFind(n)
        uf2 = UnionFind(n)
        could_delete = 0
        (num_union1, num_union2) = (0, 0)
        for (i, edge) in enumerate(edges):
            if edge[0] == 1:
                could_union = uf1.union(edge[1] - 1, edge[2] - 1)
                num_union1 += could_union
            elif edge[0] == 2:
                could_union = uf2.union(edge[1] - 1, edge[2] - 1)
                num_union2 += could_union
            else:
                could_union1 = uf1.union(edge[1] - 1, edge[2] - 1)
                could_union2 = uf2.union(edge[1] - 1, edge[2] - 1)
                num_union1 += could_union1
                num_union2 += could_union2
                could_union = could_union1 and could_union2
            could_delete += 1 - could_union
        if num_union1 != n - 1 or num_union2 != n - 1:
            return -1
        return could_delete
