class Solution:
    def reachableNodes(self, edges: List[List[int]], M: int, N: int) -> int:
        g = [[] for _ in range(N)]
        for i,j,k in edges: 
            g[i].append((j,k))
            g[j].append((i,k))
            
        q = [(-M, 0)]
        HP = [-sys.maxsize] * N
        ans = 0
        while q:
            hp, cur = heapq.heappop(q)            
            if HP[cur] != -sys.maxsize: continue
            hp *= -1
            HP[cur] = hp
            ans += 1
            for nxt, nxt_hp in g[cur]:
                nxt_hp = hp - nxt_hp - 1
                if nxt_hp < 0 or HP[nxt] != -sys.maxsize: continue
                heapq.heappush(q, (-nxt_hp, nxt))
                
        for i,j,k in edges:
            uv = 0 if HP[i] == -sys.maxsize else HP[i]
            vu = 0 if HP[j] == -sys.maxsize else HP[j]
            ans += min(k, uv + vu)
        return ans
