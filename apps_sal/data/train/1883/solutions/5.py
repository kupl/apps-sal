class Solution:
    '''
    - need to measure the the count of non-obstacles first O(n)
    - can use backtracking at each step
    - can go all directions, except if there is an obstacle or already visited
    - need to count how many available spots left, if we reach end, and spots left == 0, count as 1
    - O(3^n) time | O(n) space .. since we have n decisions at every step
    '''

    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def traverse(row, col, spacesLeft):
            # end case
            if spacesLeft == 1 and grid[row][col] == 2:
                self.results += 1
                return

            # visit current
            temp = grid[row][col]
            grid[row][col] = '#'
            spacesLeft -= 1

            # visit next in all directions
            for rowOffset, colOffset in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                nextRow, nextCol = row + rowOffset, col + colOffset
                # don't traverse if out of range
                if nextRow < 0 or nextRow == rows or nextCol < 0 or nextCol == cols:
                    continue
                # don't traverse if obstacle or visited
                if grid[nextRow][nextCol] == -1 or grid[nextRow][nextCol] == '#':
                    continue
                traverse(nextRow, nextCol, spacesLeft)

            # backtrack
            grid[row][col] = temp

        rows, cols = len(grid), len(grid[0])
        spaces = 0
        # get data from grid first
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] >= 0:
                    spaces += 1
                if grid[row][col] == 1:
                    start = (row, col)

        self.results = 0
        traverse(start[0], start[1], spaces)
        return self.results
