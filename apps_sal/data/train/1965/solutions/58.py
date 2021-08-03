from collections import deque


class UnionFind:
    def __init__(self, nodes):
        self.parent = {n: None for n in nodes}
        self.size = {n: 1 for n in nodes}

    def find_parent(self, node):
        path = []

        while self.parent[node] is not None:
            path.append(node)
            node = self.parent[node]

        for n in path:
            self.parent[n] = node

        return node

    def connected(self, a, b):
        return self.find_parent(a) == self.find_parent(b)

    def connect(self, a, b):
        a = self.find_parent(a)
        b = self.find_parent(b)

        if a != b:
            if self.size[a] > self.size[b]:
                self.parent[b] = a
                self.size[a] += self.size[b]
            else:
                self.parent[a] = b
                self.size[b] += self.size[a]


def min_spanning_tree(uf, nodes, edges):
    result = []
    for e in edges:
        t, a, b = tuple(e)

        if uf.connected(a, b):
            continue
        else:
            uf.connect(a, b)
            result.append(e)
    return result


class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        nodes = list(range(1, n + 1))
        uf_alice = UnionFind(nodes)
        uf_bob = UnionFind(nodes)

        common_edges = min_spanning_tree(uf_alice, nodes, [e for e in edges if e[0] == 3])
        min_spanning_tree(uf_bob, nodes, [e for e in edges if e[0] == 3])

        alice_edges = min_spanning_tree(uf_alice, nodes, [e for e in edges if e[0] == 1])
        bob_edges = min_spanning_tree(uf_bob, nodes, [e for e in edges if e[0] == 2])

        if uf_alice.size[uf_alice.find_parent(1)] < n or uf_bob.size[uf_bob.find_parent(1)] < n:
            return -1

        return len(edges) - (len(common_edges) + len(alice_edges) + len(bob_edges))
