class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        d = collections.defaultdict(list)
        m = {}
        for i in range(len(points)):
            m[(points[i][0], points[i][1])] = i
        h = []
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x1, y1 = points[i][0], points[i][1]
                x2, y2 = points[j][0], points[j][1]
                k = self.manhattan(x1, y1, x2, y2)
                d[m[(x1, y1)]].append([m[(x2, y2)], k])
                d[m[(x2, y2)]].append([m[(x1, y1)], k])

        ans = 0
        h = []
        for n, w in d[0]:
            h.append([w, n])
        heapq.heapify(h)
        seen = set({0})
        while h:
            w, n = heapq.heappop(h)
            if n in seen:
                continue
            seen.add(n)
            ans += w
            if len(seen) == len(points):
                break
            for n2, w2 in d[n]:
                heapq.heappush(h, [w2, n2])
        return ans

    def manhattan(self, x1, y1, x2, y2):
        return abs(x2 - x1) + abs(y2 - y1)
