class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0 if k >= grid[0][0] else -1
        nextIterations = [(0, 0, k)]
        visited = {}
        count = 0
        while len(nextIterations) > 0:
            newNextIteration = []
            for it in nextIterations:
                directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
                for dir in directions:
                    newRow = it[0] + dir[0]
                    newCol = it[1] + dir[1]
                    if newRow >= 0 and newCol >= 0 and (newRow < len(grid)) and (newCol < len(grid[0])):
                        if newRow == len(grid) - 1 and newCol == len(grid[0]) - 1:
                            if grid[newRow][newCol] == 0 or it[2] > 0:
                                return count + 1
                        if it[2] - grid[newRow][newCol] >= 0:
                            if (newRow, newCol) not in visited or visited[newRow, newCol] < it[2] - grid[newRow][newCol]:
                                newNextIteration.append((newRow, newCol, it[2] - grid[newRow][newCol]))
                                visited[newRow, newCol] = it[2] - grid[newRow][newCol]
            count += 1
            nextIterations = newNextIteration
        return -1
