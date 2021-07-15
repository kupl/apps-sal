class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        R, C = len(A), len(A[0])
        dist = [[float('inf')] * C for _ in range(R)]
        directs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        src = None
        for r in range(R):
            for c in range(C):
                if A[r][c] == 1:
                    dist[r][c] = 0
                    src = (r, c)
                if src:
                    break
            if src:
                break

        queue = [(0, r, c)]
        
        while queue:
            d, r, c = heapq.heappop(queue)

            for dr, dc in directs:
                nr, nc = r+dr, c+dc
                if not (0 <= nr < R and 0 <= nc < C):
                    continue
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
