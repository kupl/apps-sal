class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        edges.sort(key=lambda edge: -edge[0])
        ds_alice = DisjointSets(n)
        ds_bob = DisjointSets(n)
        edges_added = 0
        for e_type, u, v in edges:
            if e_type == 3:
                edges_added += int(ds_alice.union(u - 1, v - 1) | ds_bob.union(u - 1, v - 1))
            elif e_type == 2:
                edges_added += int(ds_bob.union(u - 1, v - 1))
            else:
                edges_added += int(ds_alice.union(u - 1, v - 1))
        return len(edges) - edges_added if ds_alice.isConnected() and ds_bob.isConnected() else -1


class DisjointSets:
    def __init__(self, n: int) -> None:
        self.parent = [x for x in range(n)]
        self.set_size = n

    def union(self, x: int, y: int) -> bool:
        x = self.find(x)
        y = self.find(y)
        if x != y:
            self.parent[x] = y
            self.set_size -= 1
            return True
        return False

    def find(self, x: int) -> int:
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def isConnected(self) -> bool:
        return self.set_size == 1
