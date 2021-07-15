class Solution:
    def minCostConnectPoints(self, p: List[List[int]]) -> int:
        
        ans, N, heap = 0, len(p), [(0, (0, 0))]
        seen = set()
        
        while len(seen) < N:
            w, (u, v) = heapq.heappop(heap)
            if u in seen and v in seen: continue
            seen.add(v)
            ans += w
            for j, (nx, ny) in enumerate(p):
                if j not in seen and j!=v:
                    heapq.heappush(heap, (abs(nx-p[v][0])+abs(ny-p[v][1]), (v, j)))
        return ans
