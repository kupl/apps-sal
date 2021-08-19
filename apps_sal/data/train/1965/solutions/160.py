class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        sets = [-1] * (n + 1)

        def root(v):
            if sets[v] < 0:
                return v
            sets[v] = root(sets[v])
            return sets[v]

        def union(u, v):
            (u, v) = (root(u), root(v))
            if u == v:
                return False
            if sets[u] > sets[v]:
                (u, v) = (v, u)
            sets[u] += sets[v]
            sets[v] = u
            return True
        remove_edges = 0
        (alice_edges, bob_edges) = (0, 0)
        for (t, u, v) in edges:
            if t != 3:
                continue
            if not union(u, v):
                remove_edges += 1
            else:
                alice_edges += 1
                bob_edges += 1
        save_sets = sets[:]
        for (t, u, v) in edges:
            if t != 1:
                continue
            if not union(u, v):
                remove_edges += 1
            else:
                alice_edges += 1
        sets = save_sets
        for (t, u, v) in edges:
            if t != 2:
                continue
            if not union(u, v):
                remove_edges += 1
            else:
                bob_edges += 1
        if bob_edges != n - 1 or alice_edges != n - 1:
            return -1
        return remove_edges
