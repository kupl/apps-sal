class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        l = len(points)
        if (l == 1):
            return 0        
        segs = []
        
        for idx1 in range(l):            
            for idx2 in range(idx1+1, l):
                dist = abs(points[idx1][0] - points[idx2][0]) + abs(points[idx1][1] - points[idx2][1])
                segs.append((idx1, idx2, dist))

        segs.sort(key = lambda x: x[2])

        parent = [x for x in range(l)]
        
        def getParent(idx:int) -> int:
            if parent[idx] == idx:
                return idx
            return getParent(parent[idx])
        
        self.f = 1
        def union(idx1:int, idx2:int, price:int) -> int:
            p1 = getParent(idx1)
            p2 = getParent(idx2)
            
            if (p1 == p2):
                return 0
            else:
                if (self.f == 0):
                    parent[p2] = p1
                else:
                    parent[p1] = p2
                self.f = 1 - self.f
                return price        
        
        ans = 0 
        
        lines = 0
        while(segs and lines < l - 1):
            s = segs.pop(0)
            off = union(s[0], s[1], s[2])
            ans += off
            if (off > 0):
                lines += 1
            
            
        return ans
            
            
                

