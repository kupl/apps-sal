class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = [False] * n
        dist = collections.defaultdict(list)
        for i in range(n):
            (p1, p2) = points[i]
            for j in range(n):
                (x, y) = points[j]
                dist[i].append((abs(p1 - x) + abs(p2 - y), j))
        visited[0] = True
        hp = dist[0]
        heapq.heapify(hp)
        res = count = 0
        while hp:
            (cost, cur) = heapq.heappop(hp)
            if visited[cur]:
                continue
            visited[cur] = True
            res += cost
            count += 1
            if count == n - 1:
                break
            for d in dist[cur]:
                heapq.heappush(hp, d)
        return res
