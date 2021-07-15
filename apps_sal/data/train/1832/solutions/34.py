class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = [[] for _ in range(N)]
        for i,j,n in edges:
            g[i].append((j,n))
            g[j].append((i,n))
        
        q = [(-M, 0)]
        visited = [None] * N
        ans = 0
        while q:
            hp, cur = heapq.heappop(q)
            if visited[cur] is not None: continue
            hp *= -1
            visited[cur] = hp
            ans += 1
            for nxt, cost in g[cur]:
                nxt_hp = hp - cost - 1
                if visited[nxt] is not None or nxt_hp < 0:                     
                    continue                
                heapq.heappush(q, (-nxt_hp, nxt))
                
        for i,j,n in edges:
            ui, uj = 0, 0
            if visited[i] is not None: ui = visited[i]
            if visited[j] is not None: uj = visited[j]
            ans += min(n, (ui+uj))
        return ans

