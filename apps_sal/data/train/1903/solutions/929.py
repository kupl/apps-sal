class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # try minimum spanning treee

        to_visit = set(range(1, len(points)))
        pq = [(abs(points[0][0] - points[x][0]) + abs(points[0][1] - points[x][1]), 0, x) for x in range(1, len(points))]
        heapq.heapify(pq)
        ans = 0
        while pq:
            cost, frm, to = heapq.heappop(pq)
            if to in to_visit:
                to_visit.remove(to)
                ans += cost
                for nei in to_visit:
                    x, y = points[nei]
                    heapq.heappush(pq, (abs(x - points[to][0]) + abs(y - points[to][1]), to, nei))

        return ans
