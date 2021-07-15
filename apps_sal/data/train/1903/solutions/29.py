class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        eg = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(n):
                if i != j:
                    eg[i].append([j, abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])])
        d, q = {}, [[0, 0]]
        while q:
            dis, a = heapq.heappop(q)
            if a not in d:
                d[a] = dis
                for b, c in eg[a]:
                    if b not in d:
                        heapq.heappush(q, [c, b])
        return sum(d.values())
