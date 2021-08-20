class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 0
        dis = collections.defaultdict(list)
        for i in range(n - 1):
            for j in range(i + 1, n):
                length = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dis[i].append((length, j))
                dis[j].append((length, i))
        visit = {0}
        queue = collections.deque([0])
        pull = dis[0]
        heapq.heapify(pull)
        cost = 0
        while queue and len(visit) != n:
            node = queue.popleft()
            can = heapq.heappop(pull)
            while can[1] in visit:
                can = heapq.heappop(pull)
            cost += can[0]
            for ele in dis[can[1]]:
                heapq.heappush(pull, ele)
            visit.add(can[1])
            queue.append(can[1])
        return cost
