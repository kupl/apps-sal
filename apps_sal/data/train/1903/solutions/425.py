class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def find(i):
            if parent[i] == i:
                return i
            return find(parent[i])
        def union(p1,p2):
            if size[p1] > size[p2]:
                p1,p2=p2,p1
            parent[p1] = p2
            size[p2] += size[p1]
            
        if len(points) <= 1:
            return 0
        dist = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                d = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                dist.append((d,i,j))
        dist.sort()
 
        edge = 0
        res = 0
        parent = list(range(len(points)))
        size = [1]*len(points)
        for d,n1,n2 in dist:
            p1,p2 = find(n1),find(n2)
            if p1 == p2:
                continue
            res += d
            union(p1,p2)
            edge += 1
            if edge == len(points)-1:
                return res

