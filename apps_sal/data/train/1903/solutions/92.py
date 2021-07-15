class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <=1: return 0
        minHeap = []
        for i in range(n):
            for j in range(i+1, n):
                x1, y1 = points[i]
                x2, y2 = points[j]
                dx, dy = abs(x1-x2), abs(y1-y2)
                heapq.heappush(minHeap,(dx+dy, i, j))
                
        #print(minHeap)
        
        uf = [i for i in range(n)]
        
        def find(x):
            if uf[x] == x:
                return x
            uf[x] = find(uf[x])
            return uf[x]
        
        res = 0 
        while minHeap:
            d, x, y = heapq.heappop(minHeap)
            px, py = find(x), find(y)
            if px == py:
                continue
            else:
                res += d
                uf[px] = py
        return res
