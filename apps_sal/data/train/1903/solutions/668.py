class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        
        # Prim Algo
        dist = collections.defaultdict(list)
        for i in range(n):
            p1, p2 = points[i]
            for j in range(n):
                x, y = points[j]
                dist[i].append((abs(p1-x) + abs(p2-y), j))
        visited[0] = True
        hp = dist[0]
        heapq.heapify(hp)
        res = count = 0
        while hp:
            cost, cur = heapq.heappop(hp)
            if visited[cur]: continue
            visited[cur] = True
            res += cost
            count += 1
            if count == n - 1:
                break
            for d in dist[cur]:
                heapq.heappush(hp, d)
        return res
        
        # dist = [math.inf] * n
        # cur = res = 0
        # for i in range(n-1):
        #     p1, p2 = points[cur]
        #     visited[cur] = True
        #     for j, (x, y) in enumerate(points):
        #         if not visited[j]:
        #             dist[j] = min(dist[j], abs(p1-x) + abs(p2-y))
        #     cost, cur = min([(v, k) for k, v in enumerate(dist)])
        #     dist[cur] = math.inf
        #     res += cost
        # return res

