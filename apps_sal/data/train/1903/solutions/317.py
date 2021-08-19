class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:

        ans, ct, n = 0, 0, len(p)
        seen = set()
        vertices = [(0, (0, 0))]
        def manhattan(p1, p2): return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
        while ct < n:
            # print(vertices, seen)
            w, (u, v) = heapq.heappop(vertices)
            if u in seen and v in seen:
                continue
            ans += w
            seen.add(v)
            ct += 1

            for j in range(n):
                if j not in seen and j != v:
                    heapq.heappush(vertices, (manhattan(p[j], p[v]), (v, j)))

        return ans
