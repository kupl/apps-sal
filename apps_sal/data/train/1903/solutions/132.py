class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        res = 0
        n = len(points)
        g = collections.defaultdict(list)
        tmp = []
        vst = set()
        for i in range(n):
            for j in range(n):
                if i != j and (i, j) not in vst:
                    vst.add((i, j))
                    vst.add((j, i))
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    tmp.append([i, j, dist])
        parents = [i for i in range(n)]
        ranks = [1] * n

        def find(u):
            while u != parents[u]:
                parents[u] = parents[parents[u]]
                u = parents[u]
            return u

        def union(u, v):
            (root_u, root_v) = (find(u), find(v))
            if root_u == root_v:
                return False
            if ranks[root_v] > ranks[root_u]:
                (root_u, root_v) = (root_v, root_u)
            parents[root_v] = root_u
            ranks[root_u] += ranks[root_v]
            return True
        tmp.sort(key=lambda x: x[2])
        ans = 0
        for (u, v, val) in tmp:
            if union(u, v):
                ans += val
        groups = len({find(x) for x in parents})
        return ans if groups == 1 else -1
