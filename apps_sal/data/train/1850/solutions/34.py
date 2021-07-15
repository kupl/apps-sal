class Solution:
    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:
        if N == 1:
            return [0]
        adj = [[] for _ in range(N)]
        for [u,v] in edges:
            adj[u].append(v)
            adj[v].append(u)
        d_dists = {}
        d_vertices_up_to_u = {} # better name would be d_vertices_up_to_tail instead
        sol = [0 for _ in range(N)]
        
        def dfs_dist(u,v,adj, d_dists, d_vertices_up_to_u):
            if (u,v) in d_dists:
                return d_dists[(u,v)], d_vertices_up_to_u[(u,v)]
            l_neibs = adj[u][:]
            l_neibs.remove(v)
            if len(l_neibs) == 0:
                d_dists[(u,v)] = 1
                d_vertices_up_to_u[(u,v)] = 1
                return d_dists[(u,v)], d_vertices_up_to_u[(u,v)]
            dist_u_v = 0
            vertices_up_to_u = 1 #going into (u,v)
            for nei in l_neibs:
                a,b = dfs_dist(nei,u,adj, d_dists, d_vertices_up_to_u)
                dist_u_v += a
                vertices_up_to_u += b
            dist_u_v += vertices_up_to_u
            d_dists[(u,v)] = dist_u_v
            d_vertices_up_to_u[(u,v)] = vertices_up_to_u
            return d_dists[(u,v)], d_vertices_up_to_u[(u,v)]
            
        for v in range(N):
            for u in adj[v]:
                a, _ = dfs_dist(u,v,adj, d_dists, d_vertices_up_to_u)
                sol[v] += a
        
        return sol
