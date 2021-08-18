
class Solution:
    def minCostConnectPoints(self, a: List[List[int]]) -> int:
        n, vis, ans, pq, i = len(a), set([0]), 0, [], 0
        while len(vis) < n:
            for j in range(n):
                if j not in vis:
                    heappush(pq, (abs(a[i][0] - a[j][0]) + abs(a[i][1] - a[j][1]), j))
            while pq[0][1] in vis:
                heappop(pq)
            val, i = heappop(pq)
            vis.add(i)
            ans += val
        return ans
