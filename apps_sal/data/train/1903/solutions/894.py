class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        edges = []
        arr = [-1 for _ in range(len(points))]
        def find(i):
            while arr[i]>=0:
                i = arr[i]
            return i
        
        def union(x,y):
            xp = find(x)
            yp = find(y)
            if xp==yp:
                return False
            arr[yp] = xp
            #arr[yp]-=1
            return True
        
        
        for i in range(len(points)):
            x, y = points[i]
            for j in range(i+1,len(points)):
                x1,y1 = points[j]
                edges.append([abs(x-x1)+abs(y-y1),i,j])
        edges = sorted(edges)
        res = 0
        for score,i,j in edges:
            if union(i,j):
                res+=score
        return res
