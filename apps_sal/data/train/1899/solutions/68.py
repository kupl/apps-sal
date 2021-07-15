class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        dist = [[float('inf')] * C for _ in range(R)]
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def findSrc():
            for r in range(R):
                for c in range(C):
                    if A[r][c] == 1:
                        return r, c

        r, c = findSrc()
        dist[r][c] = 0
        queue = [(0, r, c)]
        
        def neighbors(r, c):
            for nr, nc in [(r-1,c), (r+1,c), (r,c-1), (r,c+1)]:
                if 0 <= nr < R and 0 <= nc < C:
                    yield nr, nc
        
        while queue:
            d, r, c = heapq.heappop(queue)
            
            for nr, nc in neighbors(r, c):
                enqueue = False
                if A[nr][nc] == 1 and A[r][c] == 1:
                    if  d < dist[nr][nc]:
                        dist[nr][nc] = d
                        enqueue = True
                else:
                    if d + 1 < dist[nr][nc]:
                        dist[nr][nc] = d + 1
                        enqueue = True
                if enqueue:
                    heapq.heappush(queue, (dist[nr][nc], nr, nc))

        ans = float('inf')

        for r in range(R):
            for c in range(C):
                if A[r][c] == 1 and dist[r][c] > 0:
                    ans = min(ans, dist[r][c]-1)

        return ans
