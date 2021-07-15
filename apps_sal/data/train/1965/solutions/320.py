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

            # We have two nodes u and v, u in a fully-connected component A, v in another
            # fully-connected component B. A disjoint from B and u is partially connected
            # to v via an edge of `edge_type`. Since we need to reach v from u by both
            # Alice and Bob, if we can find another node, x, in A that is partially-connected 
            # to v by an edge of `needed_edge_type`, then we have edges of both types that
            # we can use to reach v from u. (use `edge_type` from u->v, or use `needed_edge_type`
            # from u->x->v). We can also try the same exercise with u and v swapped.
            needed_edge_type = 2 if edge_type == 1 else 2
            for pair in [(v0, v1), (v1, v0)]:
                u, v = pair
                found_needed_edge = False
                for x in partial_adj[needed_edge_type][v]:
                    root_x = find(p, x)
                    root_u = find(p, u)
                    if root_x == root_u:
                        # x is in in subgraph A, same as u, AND it's connected to v via the
                        # needed_edge_type
                        root_v = find(p, v)
                        union(p, rank, root_x, root_v)
                        union(p, rank, root_u, root_v)
                        nb_edges_in_mst += 2
                        found_needed_edge = True
                        break
                if found_needed_edge:
                    break

        uniq_roots = set()
        for u in range(len(p)):
            uniq_roots.add(find(p, u))
        if len(uniq_roots) != 1:
            return -1  
        
        return len(edges) - nb_edges_in_mst
            
                
            
        

