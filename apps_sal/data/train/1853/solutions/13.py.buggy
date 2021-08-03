class Solution:
    def findTheCity2(self, n: int, edges: List[List[int]], dt: int) -> int:
        \"\"\"Floyd-warshall, O(n^3)\"\"\"
        dist = [[float('inf')] * n for _ in range(n)]
        for i in range(n):
            dist[i][i] = 0
        for u, v, w in edges:
            dist[u][v] = w
            dist[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        res, con = -1, float('inf')
        for i in range(n):
            cur = sum(dist[i][j] <= dt for j in range(n))
            if cur <= con:
                con = cur
                res = i
        return res
    
    def findTheCity(self, n: int, edges: List[List[int]], dt: int) -> int:
        g = collections.defaultdict(list)
        for u, v, w in edges:
            g[u].append((v, w))
            g[v].append((u, w))
        def dijkstra(src):
            pq = [(0, src)]
            seen = set()
            res = 0
            while pq:
                d, cur = heapq.heappop(pq)
                if d > dt or cur in seen:
                    continue
                seen.add(cur)
                res += 1
                for nei, nw in g[cur]:
                    if nei not in seen:
                        heapq.heappush(pq, (d + nw, nei))
            return res
        dp = [dijkstra(i) for i in range(n)]
        mn = float('inf')
        res = -1
        for i, num in enumerate(dp):
            if num <= mn:
                mn = num
                res = i
        return res
        
                
        
                        
