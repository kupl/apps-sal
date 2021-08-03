class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
                        
        g = collections.defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
            
        def dkstr(n):
            q = [(0, n)]
            visited = set()
            while q:
                dis, node = heapq.heappop(q)
                visited.add(node)
                for adj, w in g[node]:
                    if dis+w <= distanceThreshold and adj not in visited:
                        heapq.heappush(q, (dis+w, adj))
        
            return len(visited) - 1
        
        num_city = float(\"inf\")
        ans = 0
        for i in range(n):
            num_local = dkstr(i)
            if num_local <= num_city:
                num_city = num_local
                ans = i

        return ans
        
