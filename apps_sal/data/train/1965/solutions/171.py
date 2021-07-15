class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def dfs_and_cluster(n, adj):
            num_clusters = 0
            edges_used = 0
            node_to_cluster = {}
            start_nodes = list(range(n))
            while len(start_nodes) > 0:
                node = start_nodes.pop()
                if node in node_to_cluster:
                    continue

                cluster_id = num_clusters
                num_clusters += 1

                node_to_cluster[node] = cluster_id
                q = [node]
                while len(q) > 0:
                    node = q.pop()
                    for next_node in adj[node]:
                        if next_node not in node_to_cluster:
                            edges_used += 1
                            node_to_cluster[next_node] = cluster_id
                            q.append(next_node)
            return num_clusters, node_to_cluster, edges_used

        shared_adj = {i: set() for i in range(n)}
        for edge_type, u, v in edges:
            u, v = u - 1, v - 1
            if edge_type == 3:
                shared_adj[u].add(v)
                shared_adj[v].add(u)

        shared_num_clusters, shared_node_to_cluster, shared_edges_used = dfs_and_cluster(n, shared_adj)
        print(shared_node_to_cluster)

        alice_adj = {i: set() for i in range(shared_num_clusters)}
        for edge_type, u, v in edges:
            u, v = u - 1, v - 1
            if edge_type == 1:
                u = shared_node_to_cluster[u]
                v = shared_node_to_cluster[v]
                alice_adj[u].add(v)
                alice_adj[v].add(u)

        alice_num_clusters, _, alice_edges_used = dfs_and_cluster(shared_num_clusters, alice_adj)

        bob_adj = {i: set() for i in range(shared_num_clusters)}
        for edge_type, u, v in edges:
            u, v = u - 1, v - 1
            if edge_type == 2:
                u = shared_node_to_cluster[u]
                v = shared_node_to_cluster[v]
                bob_adj[u].add(v)
                bob_adj[v].add(u)
        
        bob_num_clusters, _, bob_edges_used = dfs_and_cluster(shared_num_clusters, bob_adj)

        if alice_num_clusters > 1 or bob_num_clusters > 1:
            return -1

        return len(edges) - shared_edges_used - alice_edges_used - bob_edges_used

