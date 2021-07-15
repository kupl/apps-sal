class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        h = []
        visited = set()
        
        parent = [i for i in range(len(points))]
        rank = [0] * len(points)
        def find(i):
            if parent[i] == i:
                return i
            p = find(parent[i])
            parent[i] = p
            return p
        
        def union(a,b):
            pa, pb = find(a), find(b)
            if rank[pa]>rank[pb]:
                parent[pb] = pa
            elif rank[pb]>rank[pa]:
                parent[pa] = pb
            else:
                parent[pb] = pa
                rank[pa] +=1
        
            
        
        def dist(a,b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])
        
        for i in range(len(points)):
            for j in range(i):
                h.append((dist(points[i], points[j]), i,j))
        heapq.heapify(h)
        total = 0
        while h and len(visited) < len(points):
            dist, i,j = heapq.heappop(h)
            if find(i) != find(j):
                union(i,j)
                total +=dist

        return total
                
            

