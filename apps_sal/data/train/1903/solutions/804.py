from collections import deque

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        dist = []
        for x, i in enumerate(points):
            for y, j in enumerate(points):
                dist.append((abs(i[0] - j[0]) + abs(i[1] - j[1]), x, y))
        
        dist.sort()
        dist = deque(dist)
        
        parents = [-1 for _ in range(len(points))]
        
        def findParent(i):
            if parents[i] == -1:
                return i
            else:
                return findParent(parents[i])
        
        ans = 0
        n = 0
        while n < len(points) - 1:
            a, b, c = dist.popleft()
            bParent = findParent(b)
            cParent = findParent(c)
            if bParent == cParent:
                continue
            else:
                parents[bParent] = cParent
                ans += a
                n += 1
        
        return ans
