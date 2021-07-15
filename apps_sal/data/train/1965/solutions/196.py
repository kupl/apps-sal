'''
n is the number of nodes
if 1 < value of nodes <= n
Krustal O(ElogE)

rank[node]: the longth depth of node's children
'''

class Solution:
    def maxNumEdgesToRemove(self, n, edges):
        # Union find
        def find(node):
            if node != parent[node]:
                parent[node] = find(parent[node])
            return parent[node]

        def union(node1, node2):
            parent1, parent2 = find(node1), find(node2)
            if parent1 == parent2: return 0
            if rank[parent1] > rank[parent2]:
                parent[parent2] = parent1
            elif rank[parent1] == rank[parent2]:
                parent[parent2] = parent1
                rank[parent1] += 1
            else:
                parent[parent1] = parent2 
            
            return 1

        res = union_times_A = union_times_B = 0

        # Alice and Bob
        parent = [node for node in range(n + 1)]
        rank = [0 for node in range(n + 1)]
        
        for t, node1, node2 in edges:
            if t == 3:
                if union(node1, node2):
                    union_times_A += 1
                    union_times_B += 1
                else:
                    res += 1
        parent0 = parent[:]  # Alice union will change the parent array, keep origin for Bob

        # only Alice
        for t, node1, node2 in edges:
            if t == 1:
                if union(node1, node2):
                    union_times_A += 1
                else:
                    res += 1

        # only Bob
        parent = parent0
        for t, node1, node2 in edges:
            if t == 2:
                if union(node1, node2):
                    union_times_B += 1
                else:
                    res += 1
# only if Alice and Bob both union n-1 times, the graph is connected for both of them
        return res if union_times_A == union_times_B == n - 1 else -1
