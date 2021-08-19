class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        queue = [[0, 0, 0, k]]
        (row, col) = (len(grid), len(grid[0]))
        visit = set()
        while queue:
            (step, x, y, ob) = heapq.heappop(queue)
            if x == row - 1 and y == col - 1:
                return step
            if (x, y, ob) not in visit:
                visit.add((x, y, ob))
                for (m, n) in [[x + 1, y], [x - 1, y], [x, y + 1], [x, y - 1]]:
                    if 0 <= m < row and 0 <= n < col:
                        if not grid[x][y]:
                            heapq.heappush(queue, [step + 1, m, n, ob])
                        elif ob:
                            heapq.heappush(queue, [step + 1, m, n, ob - 1])
        return -1
