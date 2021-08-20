class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        parent = [i for i in range(len(points))]
        size = [1 for _ in range(len(points))]

        def root(p):
            while parent[p] != p:
                parent[p] = parent[parent[p]]
                p = parent[p]
            return p

        def union(p, q):
            (root_p, root_q) = (root(p), root(q))
            if root_p != root_q:
                if size[root_p] < size[root_q]:
                    parent[root_p] = root_q
                    size[root_q] += size[root_p]
                else:
                    parent[root_q] = root_p
                    size[root_p] += size[root_q]

        def connected(p, q):
            return root(p) == root(q)
        p = points
        ans = 0

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        d = [[(0, _)] * len(p) for _ in range(len(p))]
        heap = []
        for i in range(len(p)):
            for j in range(i + 1, len(p)):
                temp = dist(p[i], p[j])
                d[i][j] = (temp, j)
                d[j][i] = (temp, i)
                heappush(heap, (temp, (i, j)))
        while heap:
            (dis, (i, j)) = heappop(heap)
            if not connected(i, j):
                ans += dis
                union(i, j)
        return ans
