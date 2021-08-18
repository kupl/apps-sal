class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def find(p, u):
            parent = p[u]
            if parent == u:
                return parent

            p[u] = find(p, parent)
            return p[u]

        def union(p, rank, root_u, root_v):
            if rank[root_u] < rank[root_v]:
                p[root_u] = root_v
            elif rank[root_v] < rank[root_u]:
                p[root_v] = root_u
            else:
                p[root_u] = root_v
                rank[root_v] += 1

        p = list(range(n))
        rank = [0] * n

        full_edges = set()
        partial_edges = set()
        partial_adj = {}
        partial_adj[1] = collections.defaultdict(set)
        partial_adj[2] = collections.defaultdict(set)
        for e in edges:
            edge_type, u, v = e[0], e[1] - 1, e[2] - 1
            if edge_type == 3:
                full_edges.add((u, v))
            else:
                partial_edges.add((edge_type, u, v))
                partial_adj[edge_type][u].add(v)
                partial_adj[edge_type][v].add(u)

        nb_edges_in_mst = 0
        for e in full_edges:
            u, v = e
            root_u, root_v = find(p, u), find(p, v)
            if root_u != root_v:
                union(p, rank, root_u, root_v)
                nb_edges_in_mst += 1

        for e in partial_edges:
            edge_type, v0, v1 = e
            if find(p, v0) == find(p, v1):
                continue

            needed_edge_type = 2 if edge_type == 1 else 2
            for pair in [(v0, v1), (v1, v0)]:
                u, v = pair
                root_x = None
                for x in partial_adj[needed_edge_type][v]:
                    if find(p, x) == find(p, u):
                        root_x = find(p, x)
                        break
                if root_x != None:
                    root_u = find(p, u)
                    root_v = find(p, v)
                    union(p, rank, root_x, root_v)
                    union(p, rank, root_u, root_v)
                    nb_edges_in_mst += 2
                    break

        uniq_roots = set()
        for u in range(len(p)):
            uniq_roots.add(find(p, u))
        if len(uniq_roots) != 1:
            return -1

        return len(edges) - nb_edges_in_mst
