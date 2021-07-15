class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for i, j, w in edges:
            graph[i].append((j, w))
            graph[j].append((i, w))
        
        result = []
        for i in range(n):
            queue = [(0, i)]
            distances = defaultdict(lambda: distanceThreshold)
            visited = set()
            while queue:
                distance, i = heapq.heappop(queue)
                if i in visited:
                    continue
                visited.add(i)
                for j, w in graph[i]:
                    new_distance = distance + w
                    if new_distance <= distances[j] and j not in visited:
                        distances[j] = new_distance
                        heapq.heappush(queue, (new_distance, j))
            result.append(len(visited))
        return min(list(range(n)), key=lambda x: (result[x], -x))
        
        
        
#         dp = [[float(\"inf\")] * n for _ in range(n)]
#         for i in range(n):
#             dp[i][i] = 0
#         for i, j, w in edges:
#             dp[i][j] = w
#             dp[j][i] = w
#         for i in range(n):
#             for j in range(n):
#                 if i != j:
#                     for k in range(j + 1, n):
#                         dp[j][k] = min(dp[j][k], dp[j][i] + dp[i][k])
#                         dp[k][j] = dp[j][k]
#         return min(range(n), key=lambda i: (sum(dist <= distanceThreshold for dist in dp[i]), -i))
        
        
        
#         graph = [[] for _ in range(n)]
#         for i, j, w in edges:
#             graph[i].append((j, w))
#             graph[j].append((i, w))
        
#         result = []
#         for i in range(n):
#             queue = [(0, i)]
#             visited = set()
#             while queue:
#                 distance, i = heapq.heappop(queue)
#                 if i in visited:
#                     continue
#                 visited.add(i)
#                 for j, w in graph[i]:
#                     if distance + w <= distanceThreshold:
#                         heapq.heappush(queue, (distance + w, j))
#             visited.remove(i)
#             result.append(list(visited))
#         return min(range(n), key=lambda x: (len(result[x]), -x))

