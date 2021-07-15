class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        heap = [[0,-k,0,0]]
        seen = set()
        while heap:
            step, block, i, j = heappop(heap)
            
            if (i,j,block) in seen:
                continue
            seen.add((i,j,block))
            
            if (i,j) == (m-1,n-1):
                return step
            
            for ni,nj in [[i+1,j], [i-1,j], [i,j+1], [i,j-1]]:
                if 0 <= ni < m and 0 <= nj < n:
                    if grid[ni][nj] == 0:
                        if (ni,nj,block) not in seen:
                            heappush(heap, [step+1, block, ni, nj])
                    elif block + 1 <= 0 and (ni,nj,block+1) not in seen:
                        heappush(heap, [step+1, block+1, ni, nj])
        return -1
