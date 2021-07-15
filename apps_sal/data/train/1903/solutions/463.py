class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        N = len(points)
        def distance(p1, p2):
            return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        
        ans = 0
        h = []
        heappush(h, (0, points[0]))
        visited = set()
        
        while h:
            d, p = heappop(h)
            if (p[0], p[1]) in visited:
                continue
            visited.add((p[0], p[1]))
            ans += d
            
            for point in points:
                if (point[0], point[1]) not in visited:
                    heappush(h, (distance(p, point), point))
                    
            if len(visited) == N:
                break
                
        return ans
                    
        
    def minCostConnectPoints_2(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i+1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt+1, ans+d
                for record in c[j]: heapq.heappush(heap, record)
            if cnt >= n: break        
        return ans  
        

