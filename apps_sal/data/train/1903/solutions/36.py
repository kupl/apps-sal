class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # # https://leetcode.com/problems/min-cost-to-connect-all-points/discuss/843995/Python-3-or-Min-Spanning-Tree-or-Prim's-Algorithm
        # manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        # n, c = len(points), collections.defaultdict(list)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         d = manhattan(points[i], points[j])
        #         c[i].append((d, j))
        #         c[j].append((d, i))
        # cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        # visited[0] = 1
        # heapq.heapify(heap)
        # while heap:
        #     d, j = heapq.heappop(heap)
        #     if not visited[j]:
        #         visited[j], cnt, ans = 1, cnt+1, ans+d
        #         for record in c[j]: heapq.heappush(heap, record)
        #     if cnt >= n: break
        # return ans

        n = len(points)
        if len(points) == 1:
            return 0
        res = 0
        curr = 0  # select a random point as the starting point
        dis = [math.inf] * n
        explored = set()

        for _ in range(n - 1):
            x0, y0 = points[curr]
            explored.add(curr)
            for j, (x, y) in enumerate(points):
                if j in explored:
                    continue
                dis[j] = min(dis[j], abs(x - x0) + abs(y - y0))
            delta, curr = min((d, j) for j, d in enumerate(dis))
            dis[curr] = math.inf
            res += delta

        return res
