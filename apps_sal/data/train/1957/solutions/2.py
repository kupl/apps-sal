class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if not grid:
            return -1
        onesDict = {(0, 0): 0}
        m, n = len(grid), len(grid[0])
        heap = [(self.distance(m, n, 0, 0), 0, 0, 0, 0)]
        heapq.heapify(heap)
        
        while heap:
            curHue, steps, row, col, ones = heapq.heappop(heap)
            if (row, col) == (m - 1, n -1):
                return curHue
            for y, x in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                r, c = row + y, col + x
                if 0 <= r < m and 0 <= c < n:
                    totalOnes = ones + grid[r][c]
                    if totalOnes < onesDict.get((r,c), k + 1):
                        heapq.heappush(heap, (steps + 1 + self.distance(m, n, r, c), steps + 1, r, c, totalOnes))
                        onesDict[(r, c)] = totalOnes
        return -1
        
    def distance(self, m, n, y, x):
        return m + n - y - x - 2
