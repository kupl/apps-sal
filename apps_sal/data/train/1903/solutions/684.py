class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        d = collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                d[i].append((dist, i, j))
                d[j].append((dist, j, i))
        chosen = {0}
        between = d[0].copy()
        heapq.heapify(between)
        res = 0
        while len(chosen) < n:
            (dist, i, j) = heapq.heappop(between)
            if i in chosen and j in chosen:
                continue
            elif i in chosen and j not in chosen:
                chosen.add(j)
                res += abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                for (jd, js, je) in d[j]:
                    heapq.heappush(between, (jd, js, je))
            elif i not in chosen and j in chosen:
                chosen.add(i)
                res += abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                for (iid, iis, iie) in d[i]:
                    heapq.heappush(between, (iid, iis, iie))
        return res
