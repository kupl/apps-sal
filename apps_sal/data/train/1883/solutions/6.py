class Solution:
    """
    - need to measure the the count of non-obstacles first O(n)
    - can use backtracking at each step
    - can go all directions, except if there is an obstacle or already visited
    - need to count how many available spots left, if we reach end, and spots left == 0, count as 1
    - O(3^n) time | O(n) space .. since we have n decisions at every step
    """

    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        def traverse(row, col, spacesLeft):
            nonlocal results
            if spacesLeft == 1 and grid[row][col] == 2:
                results += 1
                return
            temp = grid[row][col]
            grid[row][col] = '#'
            spacesLeft -= 1
            for (rowOffset, colOffset) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                (nextRow, nextCol) = (row + rowOffset, col + colOffset)
                if nextRow < 0 or nextRow == rows or nextCol < 0 or (nextCol == cols):
                    continue
                if grid[nextRow][nextCol] == -1 or grid[nextRow][nextCol] == '#':
                    continue
                traverse(nextRow, nextCol, spacesLeft)
            grid[row][col] = temp
        (rows, cols) = (len(grid), len(grid[0]))
        spaces = 0
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] >= 0:
                    spaces += 1
                if grid[row][col] == 1:
                    start = (row, col)
        results = 0
        traverse(start[0], start[1], spaces)
        return results
