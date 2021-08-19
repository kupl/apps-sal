class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 1:
            return 0

        def calc_mahattan_dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
        edge_weights = [calc_mahattan_dist(points[ix], points[iy]) for ix in range(n) for iy in range(ix + 1, n)]
        (ixy2idx_mapping, idx2ixy_mapping) = (dict(), dict())
        idx = 0
        for ix in range(n):
            for iy in range(ix + 1, n):
                ixy2idx_mapping[ix, iy] = idx
                idx2ixy_mapping[idx] = (ix, iy)
                idx += 1

        def ixy2idx(ix, iy):
            (ix_, iy_) = [x([ix, iy]) for x in [min, max]]
            return ixy2idx_mapping[ix, iy]

        def idx2ixy(idx):
            return idx2ixy_mapping[idx]
        groups = list(range(n))
        sizes = [1 for _ in range(n)]

        def find(ix):
            while ix != groups[ix]:
                ix = groups[ix]
            return ix

        def union(ix, iy):
            (root1, root2) = list(map(find, [ix, iy]))
            if root1 == root2:
                return
            (size1, size2) = [sizes[x] for x in [root1, root2]]
            comp = [(size1, root1), (size2, root2)]
            (min_root, max_root) = [x(comp)[1] for x in [min, max]]
            groups[min_root] = max_root
            sizes[max_root] += sizes[min_root]
        (__, edge_index_argsort) = list(map(list, list(zip(*sorted(list(zip(edge_weights, list(range(len(edge_weights))))))))))
        min_cost = 0
        for eix in edge_index_argsort:
            edge_weight = edge_weights[eix]
            (node1, node2) = idx2ixy(eix)
            if find(node1) == find(node2):
                continue
            min_cost += edge_weight
            union(node1, node2)
        return min_cost
