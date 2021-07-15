class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        cache = {}
        for i, coord in enumerate(points):
            cache[i] = coord
        
        # print(cache)

            
        def compute(p1, p2):
            x1, y1 = cache[p1]
            x2, y2 = cache[p2]
            return abs(x1-x2) + abs(y1-y2)
        
        edges = []
        for x, y in combinations(list(cache.items()), 2):
            edges.append((compute(x[0], y[0]), x[0], y[0]))
        
        # print(edges)
        
        edges.sort(reverse=True)
        
        # print(edges)
        
        ans = 0
        L = len(cache)
        
        parents = list(range(L))
        
        def union(x, y):
            parents[find(x)] = find(y)
        
        def find(x):
            if parents[x] != x:
                parents[x] = find(parents[x])
            
            return parents[x]
        
        if L == 1:
            return 0

        while edges:
            cost, n1, n2 = edges.pop()
            
            if find(n1) != find(n2):
                union(n1, n2)
                ans += cost
            
        return ans
            
            
            

#         for n, coord in cache.items():
#             print(n, parents)

#             closest_point = None
#             closest_cost = float('inf')
#             for i in range(L):
#                 if n == i:
#                     continue  # skip self

#                 dist = compute(n, i)

#                 # print('checking cost to', i, '...', dist)
#                 if dist < closest_cost:
#                     closest_cost = dist
#                     closest_point = i

#             if find(n) != find(closest_point):
#                 union(n, closest_point)
#                 cost += closest_cost
#                 print('connecting', n, 'and', closest_point)
        
#         # print(parents)
        
#         return cost

