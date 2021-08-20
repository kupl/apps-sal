class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def find(symbol):
            if group_map.get(symbol) is None:
                group_map[symbol] = symbol
                return group_map[symbol]
            root = symbol
            while root != group_map[root]:
                root = group_map[root]
            while symbol != root:
                parent = group_map[symbol]
                group_map[symbol] = root
                symbol = parent
            return root

        def union(symbol1, symbol2):
            root1 = find(symbol1)
            root2 = find(symbol2)
            if root1 == root2:
                return
            if group_size.get(root1) is None:
                group_map[root1] = root1
                group_size[root1] = 1
            if group_size.get(root2) is None:
                group_map[root2] = root2
                group_size[root2] = 1
            if group_size[root1] < group_size[root2]:
                group_size[root2] += group_size[root1]
                group_map[root1] = root2
            else:
                group_size[root1] += group_size[root2]
                group_map[root2] = root1
        all_edges = []
        for i in range(0, len(points)):
            for j in range(i + 1, len(points)):
                all_edges.append((i, j, abs(points[j][0] - points[i][0]) + abs(points[j][1] - points[i][1])))
        all_edges.sort(key=lambda x: x[2])
        vertices = [i for i in range(0, len(points))]
        group_map = {}
        group_size = {}
        edge_count = 0
        edge_index = 0
        total_weight = 0
        while edge_count < len(points) - 1:
            (node_1, node_2, weight) = all_edges[edge_index]
            edge_index += 1
            parent_1 = find(node_1)
            parent_2 = find(node_2)
            if parent_1 != parent_2:
                edge_count += 1
                total_weight += weight
                union(parent_1, parent_2)
        return total_weight
