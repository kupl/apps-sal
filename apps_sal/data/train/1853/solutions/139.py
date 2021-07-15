class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        
        graph = defaultdict(list)
        output = []
        
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        for i in range(n):
            
            #distance , node
            queue = [(i, 0)]
            curr = {}
            
            while queue:
                node, dist = heapq.heappop(queue)
                
                if node in curr and dist >= curr[node]:
                    continue
                
                curr[node] = dist
                
                for nei, newDist in graph[node]:
                    if newDist + dist <= distanceThreshold:
                        heapq.heappush(queue,(nei, newDist + dist))
            
            output.append(len(curr)-1)
        
        for node in reversed(range(len(output))):
            if output[node] == min(output):
                return node
