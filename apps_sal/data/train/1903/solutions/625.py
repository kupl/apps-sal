class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        import heapq
        stack = []
        ans = 0
        used = set([0])
        ps = set([0])

        while ps:
            i = ps.pop()
            for j in range(len(points)):
                if i != j and j not in used:
                    dist = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                    heappush(stack, (dist, i, j))

            while stack:
                dist, x, y = heappop(stack)

                if x in used and y not in used:
                    ans += dist
                    used.add(y)
                    ps.add(y)
                    break

                elif y in used and x not in used:
                    ans += dist
                    used.add(x)
                    ps.add(x)
                    break

        return ans
