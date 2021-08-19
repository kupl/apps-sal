class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        def cal(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        (d, q) = ({}, [[0, 0]])
        ans = 0
        while q:
            (dis, a) = heapq.heappop(q)
            if a not in d:
                d[a] = dis
                ans += dis
                for b in range(len(points)):
                    if b not in d:
                        heapq.heappush(q, [cal(points[a], points[b]), b])
        return ans
