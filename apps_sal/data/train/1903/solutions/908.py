class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        self.parent = list(range(len(points)))
        self.rank = [1]*len(points)
        
        def find(a):
            if self.parent[a] != a:
                self.parent[a] = find(self.parent[a])
            return self.parent[a]
        
        def union(a,b):
            p1 = find(a)
            p2 = find(b)
            if p1 == p2: return False
            if self.rank[p1] > self.rank[p2]:
                self.parent[p2] = p1
            else:
                if self.rank[p1] < self.rank[p2]:
                    self.parent[p1] = p2
                else:
                    self.parent[p1] = p2
                    self.rank[p2] += 1
            return True
        
        def dist(a,b):
            return abs(a[0]-b[0])+abs(a[1]-b[1])
        
        weights = {}
        edges = []
        for i in range(len(points)):
            for j in range(i+1,len(points)):
                weights[(i,j)] = dist(points[i], points[j])
                edges.append((i,j))
        
        edges.sort(key=lambda x: weights[x])
        
        ans = 0
        
        for e in edges:
            if union(e[0],e[1]):
                ans += weights[e]
                
        return ans
        

