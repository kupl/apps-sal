class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        R, C = len(grid), len(grid[0])
        heap = [(0, k, 0, 0)] # length, elimination, i, j
        visited = set()
        
        while heap:
            l, e, i, j = heapq.heappop(heap)
            if i == R - 1 and j == C - 1:
                return l
            if e < 0:
                continue
            if (i, j, e) in visited:
                continue
            visited.add((i, j, e))
            for x, y in [(i+1, j), (i, j+1), (i-1, j), (i, j-1)]:
                if x < 0 or x >= R or y < 0 or y >= C:
                    continue
                heapq.heappush(heap, (l+1, e - grid[x][y], x, y))
                
        return -1
