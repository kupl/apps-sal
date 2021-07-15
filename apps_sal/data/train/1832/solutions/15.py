class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = [[] for _ in range(N)]
        for i,j,n in edges:
            g[i].append((j, n))
            g[j].append((i, n))
            
        q = [(-M, 0)]
        visited = [-10001] * N
        ans = 0
        while q:
            #print(list(q))
            hp, cur = heapq.heappop(q)
            if visited[cur] != -10001:
                #print(cur, visited[cur])
                continue
            hp = -hp
            visited[cur] = hp
            ans += 1
            for node, cost in g[cur]:
                nxt_hp = hp - cost - 1
                if nxt_hp >= 0: 
                    heapq.heappush(q, (-nxt_hp, node))                    
        
        for i,j,n in edges:
            ui, uj = 0, 0
            if visited[i] != -10001: ui = visited[i]
            if visited[j] != -10001: uj = visited[j]
            ans += min(ui+uj, n)
            
        return ans

