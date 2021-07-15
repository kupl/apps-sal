class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        graph = collections.defaultdict(list)
        for u, v, w, in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        hq = [(-M, 0)]
        hp = {}
        
        while hq:
            m, node = heapq.heappop(hq)            
            if node in hp:
                continue
            m = -m
            hp[node] = m
            
            for v, w in graph[node]:
                if m > w:
                    remains = m - w - 1
                    heapq.heappush(hq, (-remains, v))
            
        ans = len(hp)
        for u, v, w in edges:
            a = hp[u] if u in hp else 0
            b = hp[v] if v in hp else 0
            if a + b < w:
                ans += a + b
            else:
                ans += w
        return ans
