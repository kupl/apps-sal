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
            edge_type, u, v = e
            root_u, root_v = find(p, u), find(p, v)
            if root_u == root_v:
                continue

            # We have two nodes u and v such that they fall into two disjoint
            # connected sub-graphs, and u from subgraph A is connected to v
            # in subgraph B with either edge_type == 1 or edge_type 2. Since we
            # need to reach v from subgraph A by both Alice and Bob, if we can
            # find another node, x, in subgraph A that is connected to v in subgraph B
            # by the other edge_type, then we can reach v from any node in subgraph A.
            needed_edge_type = 2 if edge_type == 1 else 2
            foo = (v, root_u)
            found_needed_edge = False
            for x in partial_adj[needed_edge_type][foo[0]]:
                root_x = find(p, x)
                if root_x == foo[1]:
                    # x is in in subgraph A, same as u, AND it's connected to v via the
                    # needed_edge_type
                    union(p, rank, root_x, foo[1])
                    union(p, rank, root_u, root_v)
                    nb_edges_in_mst += 2
                    found_needed_edge = True
                    break
            if found_needed_edge:
                continue
            
            foo = (u, root_v)
            for x in partial_adj[needed_edge_type][foo[0]]:
                root_x = find(p, x)
                if root_x == foo[1]:
                    # y is in the subgraph B, same as v, and it's connected to u via the
                    # needed_edge_type
                    union(p, rank, root_x, foo[1])
                    union(p, rank, root_u, root_v)
                    nb_edges_in_mst += 2
                    break

        uniq_roots = set()
        for u in range(len(p)):
            uniq_roots.add(find(p, u))
        if len(uniq_roots) != 1:
            return -1  
        
        return len(edges) - nb_edges_in_mst
            
                
            
        

