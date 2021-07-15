class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = collections.defaultdict(dict)
        for s, e, v in edges:
            g[s][e] = g[e][s] = v
            
        dist = {0:0}
        pq = [(0, 0)]
        used = {}
        ans = 0

        
        while pq:
            
            d, node = heapq.heappop(pq)
            if d > dist[node]:
                continue
                
            ans += 1
            
            for e, w in g[node].items():
                
                v = min(w, M - d)
                used[node, e] = v
                
                d2 = d + w + 1
                if d2 < dist.get(e, M+1):
                    heapq.heappush(pq, (d2, e))
                    dist[e] = d2
                    
        for s, e, w in edges:
            ans += min(w, used.get((s, e), 0) + used.get((e, s), 0))
            
        return ans
