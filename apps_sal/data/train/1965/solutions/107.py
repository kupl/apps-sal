class DSU:

    def __init__(self):
        self.parent = {}
        self.size = {}

    def root(self, A):
        tmp = A
        while self.parent[tmp] != tmp:
            tmp = self.parent[tmp]
            self.parent[tmp] = self.parent[self.parent[tmp]]
        return tmp

    def union(self, A, B):
        if self.root(A) == self.root(B):
            return False
        else:
            if self.size[self.root(A)] >= self.size[self.root(B)]:
                self.size[self.root(A)] += self.size[self.root(B)]
                self.parent[self.root(B)] = self.root(A)
            else:
                self.size[self.root(B)] += self.size[self.root(A)]
                self.parent[self.root(A)] = self.root(B)
            return True

    def add_edge(self, A, B):
        if A not in self.parent:
            self.parent[A] = A
            self.size[A] = 1
        if B not in self.parent:
            self.parent[B] = B
            self.size[B] = 1
        return self.union(A, B)

    def get_node_count(self):
        return len(self.parent)


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges_removed = 0
        (alice_graph, bob_graph) = (DSU(), DSU())
        for (typ, u, v) in edges:
            if typ == 3:
                if not (alice_graph.add_edge(u, v) and bob_graph.add_edge(u, v)):
                    edges_removed += 1
        for (typ, u, v) in edges:
            if typ == 2:
                if not bob_graph.add_edge(u, v):
                    edges_removed += 1
            if typ == 1:
                if not alice_graph.add_edge(u, v):
                    edges_removed += 1
        if alice_graph.get_node_count() != n or bob_graph.get_node_count() != n:
            return -1
        return edges_removed
