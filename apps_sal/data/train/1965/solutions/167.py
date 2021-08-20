class Solution:

    def maxNumEdgesToRemove(self, n, edges):

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            node1_p = find(node1)
            node2_p = find(node2)
            if node1_p == node2_p:
                return False
            if rank[node1_p] > rank[node2_p]:
                parent[node2_p] = node1_p
                rank[node1_p] += 1
            else:
                parent[node1_p] = node2_p
                rank[node2_p] += 1
            return True
        parent = [i for i in range(n + 1)]
        rank = [0] * (n + 1)
        edge_added = 0
        edge_can_remove = 0
        for edge in edges:
            if edge[0] == 3:
                if union(edge[1], edge[2]):
                    edge_added += 1
                else:
                    edge_can_remove += 1
        parent_back_up = parent[:]
        alice_edge = 0
        bob_edge = 0
        for edge in edges:
            if edge[0] == 1:
                if union(edge[1], edge[2]):
                    alice_edge += 1
                else:
                    edge_can_remove += 1
        parent = parent_back_up
        for edge in edges:
            if edge[0] == 2:
                if union(edge[1], edge[2]):
                    bob_edge += 1
                else:
                    edge_can_remove += 1
        if alice_edge == bob_edge == n - 1 - edge_added and edge_can_remove >= 0:
            return edge_can_remove
        return -1
