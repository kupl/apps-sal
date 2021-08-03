class UnionFind:
    def __init__(self, n):
        self.p = {}
        self.group = n
        for i in range(1, n + 1):
            self.p[i] = i

    def unite(self, a, b):
        pa, pb = self.find(a), self.find(b)
        if pa != pb:
            self.p[pa] = pb
            self.group -= 1
            return True
        return False

    def find(self, a):
        if self.p[a] != a:
            self.p[a] = self.find(self.p[a])
        return self.p[a]

    def united(self):
        return self.group == 1


class Solution:
    # copied https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/discuss/831506/Textbook-Union-Find-Data-Structure-Code-with-Explanation-and-comments
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges = sorted(edges, reverse=True)

        edgesAdded = 0
        bob, alice = UnionFind(n), UnionFind(n)
        for edge in edges:
            tp, one, two = edge[0], edge[1], edge[2]
            if tp == 3:
                bu = bob.unite(one, two)
                au = alice.unite(one, two)
                edgesAdded += 1 if bu or au else 0
            elif tp == 2:
                edgesAdded += bob.unite(one, two)
            else:
                edgesAdded += alice.unite(one, two)

        return len(edges) - edgesAdded if bob.united() and alice.united() else -1
