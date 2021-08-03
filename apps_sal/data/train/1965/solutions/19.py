class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda x: -x[0])
        uf1 = UnionFind(n + 1)
        uf2 = UnionFind(n + 1)

        e1 = e2 = 0
        res = 0

        for type_, node1, node2 in edges:

            if type_ == 3:
                val1 = uf1.union(node1, node2)
                val2 = uf2.union(node1, node2)
                res += val1 or val2
                e1 += val1
                e2 += val2

            if type_ == 1:
                val = uf1.union(node1, node2)
                res += val
                e1 += val

            else:
                val = uf2.union(node1, node2)
                res += val
                e2 += val

        if e1 == e2 == n - 1:
            # print(res)
            return len(edges) - res
        return -1


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)

        if rootx == rooty:
            return False

        self.parent[rooty] = rootx
        return True

    def find(self, x):
        while x != self.parent[x]:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
