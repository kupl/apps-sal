class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        graph = collections.defaultdict(list)
        
        for node1, points1 in enumerate(points):
            for node2, points2 in enumerate(points):
                graph[node1].append(( abs(points1[0] - points2[0]) + abs(points1[1] - points2[1]), node2 ))
                
        pq = [(0,0)]
        res = 0
        visited = set()
        
        while pq:
            d, node = heapq.heappop(pq)
            if node in visited:
                continue
            visited.add(node)
            res += d
            if len(visited) == len(points):
                return res
            for distance,nei in graph[node]:
                if nei not in visited:
                    heapq.heappush(pq, (distance,nei))
                    
        return res
