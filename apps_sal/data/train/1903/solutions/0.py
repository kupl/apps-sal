class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        dist = [float(\"inf\")] * n
        remain = set()
        for i in range(0,n):
            remain.add(i)
        dist[0] = 0
        remain.discard(0)
        curr = 0
        res = 0
        while len(remain) > 0:
            lo = float(\"inf\")
            loind = -1
            # curr is the next lowest
            a,b = points[curr]
            for r in remain:
                x,y = points[r]
                tempdist = abs(x-a) + abs(y-b)
                if tempdist < dist[r]:
                    dist[r] = tempdist
                tempdist = dist[r]
                
                if tempdist < lo:
                    lo = tempdist
                    loind = r
            
            res += lo
            
            curr = loind
            # remove curr from remain
            remain.discard(curr)
            
        return res
            
