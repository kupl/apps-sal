class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def distance(p1,p2):
            return abs(p1[1] - p2[1]) + abs(p1[0] - p2[0])
        n = len(points)
        edges = [(i,j,distance(points[i],points[j])) for i in range(n) for j in range(i+1,n)]
        edges.sort(key=lambda x: x[2])        
        father = [i for i in range(n + 1)]
        def find(x):
            if father[x] != x:
                father[x] = find(father[x])
            return father[x]
        def union(x,y):
            x = father[x]
            y = father[y]
            if x < y:
                father[y] = x
            else:
                father[x] = y
        ans = 0
        for p1,p2,d in edges:
            if find(p1) != find(p2):
                ans += d
                union(p1,p2)
        return ans
\"\"\"
[[2,-3],[-17,-8],[13,8],[-17,-15]]
[[3,12],[-2,5],[-4,1]]
[[0,0],[2,2],[3,10],[5,2],[7,0]]
[[0,0]]
[[-1000000,-1000000],[1000000,1000000]]
[[0,0],[1,1],[1,0],[-1,1]]
[[3,12],[-2,5],[-4,1]]
\"\"\"
