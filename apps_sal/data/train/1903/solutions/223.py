class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        ss = [(0,0)]
        n = len(points)
        inc = set()
        ans = 0
        while n:
            node = heapq.heappop(ss)
            if node[1] not in inc:
                ans+=node[0]
                p1 = points[node[1]]
                for i in range(len(points)):
                    if i!=node[1] and i not in inc:
                        p2 = points[i]
                        dist = abs(p1[0]-p2[0])+abs(p1[1]-p2[1])
                        heapq.heappush(ss,(dist,i))
                inc.add(node[1])
                n-=1
        return ans
