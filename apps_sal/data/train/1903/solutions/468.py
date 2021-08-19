class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        if not points or len(points) <= 1:
            return 0
        p_dis = {}
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                p1 = points[i]
                p2 = points[j]
                dis = abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
                p_dis.setdefault(i, [])
                p_dis.setdefault(j, [])
                p_dis[i].append((dis, j))
                p_dis[j].append((dis, i))
        visited = [False] * len(points)
        visited[0] = True
        count = 1
        heap = []
        res = 0
        for (d, p) in p_dis[0]:
            heapq.heappush(heap, (d, p))
        while heap:
            (dis, p) = heapq.heappop(heap)
            if not visited[p]:
                count += 1
                visited[p] = True
                res += dis
                for (_d, _p) in p_dis[p]:
                    heapq.heappush(heap, (_d, _p))
            if count == len(points):
                break
        return res
