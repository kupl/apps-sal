class UnionNode:

    def __init__(self):
        self.parent = None
        self.order = 0


class UnionSet:

    def __init__(self, N):
        self.els = [UnionNode() for i in range(N)]
        self.edge_count = 0

    def find(self, i):
        node = self.els[i]
        if node.parent is None:
            return i
        node.parent = self.find(node.parent)
        return node.parent

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)
        if i == j:
            return
        self.edge_count += 1
        i_node = self.els[i]
        j_node = self.els[j]
        if i_node.order < j_node.order:
            (i_node, j_node) = (j_node, i_node)
            (i, j) = (j, i)
        j_node.parent = i
        i_node.order += i_node.order == j_node.order

    def connected(self):
        return len(self.els) == self.edge_count + 1


class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        alice_union = UnionSet(n)
        bob_union = UnionSet(n)
        shared_union = UnionSet(n)
        for (type_, u, v) in edges:
            if type_ in (1, 3):
                alice_union.union(u - 1, v - 1)
            if type_ in (2, 3):
                bob_union.union(u - 1, v - 1)
            if type_ == 3:
                shared_union.union(u - 1, v - 1)
        if not alice_union.connected() or not bob_union.connected():
            return -1
        missing_edges = n - 1 - shared_union.edge_count
        needed_edges = shared_union.edge_count + 2 * missing_edges
        return len(edges) - needed_edges
