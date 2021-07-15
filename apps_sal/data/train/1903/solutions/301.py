class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        manhattan = lambda p1, p2: abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])
        n, c = len(points), collections.defaultdict(list)
        for i in range(n):
            for j in range(i + 1, n):
                d = manhattan(points[i], points[j])
                c[i].append((d, j))
                c[j].append((d, i))
        cnt, ans, visited, heap = 1, 0, [0] * n, c[0]
        visited[0] = 1
        heapq.heapify(heap)
        while heap:
            d, j = heapq.heappop(heap)
            if not visited[j]:
                visited[j], cnt, ans = 1, cnt + 1, ans+d
                for record in c[j]: 
                    if not visited[record[1]]:
                        heapq.heappush(heap, record)
            if cnt >= n: break        
        return ans if cnt >= n else 0 
    
#         def manhattan(x, y):
#             return abs(x[0]-y[0]) + abs(x[1]-y[1])
        
#         ans, n = 0, len(p)
#         seen = set()
#         vertices = [(0, (0, 0))]
        
#         while len(seen) < n:
#             # print(vertices, seen)
#             w, (u, v) = heapq.heappop(vertices)            
#             if v in seen: continue
#             ans += w
#             seen.add(v)
#             for j in range(n):
#                 if j not in seen and j!=v:
#                     heapq.heappush(vertices, (manhattan(p[j], p[v]), (v, j)))

