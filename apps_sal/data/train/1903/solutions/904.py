class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def pdist(i, j):
            return abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
        N = len(points)
        pvisited = [False] * N
        h = []
        mincost = 0
        heappush(h, (0, 0))
        while h:
            dist, el = heappop(h)
            if not pvisited[el]:
                pvisited[el] = True
                mincost += dist
                for i in range(N):
                    if not pvisited[i]:
                        heappush(h, (pdist(el, i), i))
        return mincost
