class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # seems dijkstra with all the neighbors connected?
        # try minimum spanning treee
        node = 0
        # build the graph first
        seen = set([0])
        edges = [(abs(points[0][0] - points[x][0]) + abs(points[0][1] - points[x][1]), 0, x) for x in range(1, len(points))]
        heapq.heapify(edges)
        ans = 0
        while edges:
            cost, frm, to = heapq.heappop(edges)
            if to not in seen:
                seen.add(to)
                ans += cost
                for to_next, (x, y) in enumerate(points):
                    if to_next not in seen:
                        heapq.heappush(edges, (abs(x - points[to][0]) + abs(y - points[to][1]), to, to_next))

        return ans
