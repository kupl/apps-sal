class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        def union(node1, node2):
            root1, root2 = find(node1), find(node2)
            if root1 != root2:
                if rank[root1] <= rank[root2]:
                    parent[root1] = root2
                    rank[root2] += 1
                else:
                    parent[root2] = root1
                    rank[root1] += 1

        def find(node):
            if parent[node] != node:
                parent[node] = find(parent[node])
            return parent[node]

        parent, rank = {i: i for i in range(1, n + 1)}, {i: 0 for i in range(1, n + 1)}
        ans, n1, n2 = 0, 0, 0
        for t, node1, node2 in edges:
            if t == 3:
                if find(node1) != find(node2):
                    union(node1, node2)
                    n1 += 1
                    n2 += 1
                else:
                    ans += 1

        p = parent.copy()
        for t, node1, node2 in edges:
            if t == 1:
                if find(node1) != find(node2):
                    union(node1, node2)
                    n1 += 1
                else:
                    ans += 1

        parent = p
        for t, node1, node2 in edges:
            if t == 2:
                if find(node1) != find(node2):
                    union(node1, node2)
                    n2 += 1
                else:
                    ans += 1

        return ans if n1 == n2 == n - 1 else -1
