class Solution:

    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:

        def find(parent, node):
            if node != parent[node]:
                parent[node] = find(parent, parent[node])
            return parent[node]

        def union(parent, node1, node2):
            parent1 = find(parent, node1)
            parent2 = find(parent, node2)
            parent[parent2] = parent1
            return
        result = 0
        parent1 = [i for i in range(n)]
        parent2 = [i for i in range(n)]
        for edge in edges:
            if edge[0] == 3:
                if find(parent1, edge[1] - 1) == find(parent1, edge[2] - 1):
                    result += 1
                else:
                    union(parent1, edge[1] - 1, edge[2] - 1)
                    union(parent2, edge[1] - 1, edge[2] - 1)
        for edge in edges:
            if edge[0] == 1:
                if find(parent1, edge[1] - 1) == find(parent1, edge[2] - 1):
                    result += 1
                else:
                    union(parent1, edge[1] - 1, edge[2] - 1)
            if edge[0] == 2:
                if find(parent2, edge[1] - 1) == find(parent2, edge[2] - 1):
                    result += 1
                else:
                    union(parent2, edge[1] - 1, edge[2] - 1)
        root1 = find(parent1, 0)
        root2 = find(parent2, 0)
        for node in range(n):
            if find(parent1, node) != root1 or find(parent2, node) != root2:
                return -1
        return result
