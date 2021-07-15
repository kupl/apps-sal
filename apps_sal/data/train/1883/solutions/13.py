# General idea for the solution is as follows:
# 1) We traverse the whole array once initially, in doing so we find a) the location of the
#   start point, b) the location of the end point and c) the number of traversable square.
# 2) We then do a simple DFS traversal, like before. During this DFS traversal we can mark
#   previous nodes as visited in-place (replacing the original value on the backtrack).
#       - During the DFS traversal we count how many squares we have visited.
#       - We only increment the number of viable paths if we reach the end node after
#         visiting all the traversable nodes (i.e. count = 0, for example).

class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        # First, traverse the array once, finding the start location and the number of -1
        # entries
        startIndex = None
        numTraversable = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # Find the start index
                if grid[i][j] == 1:
                    startIndex = [i, j]
                # Keep track of the number of obstacles
                if grid[i][j] != -1:
                    numTraversable += 1
        # Find the number of traversable squares (n * m - numObstables - 2)
        numTraversable -= 1 # -1 for start
        # Now call your DFS function from the starting node
        numPaths = self.visitedDFS(grid, startIndex, numTraversable)
        return numPaths

    def visitedDFS(self, grid, coord, count):
        numPaths = 0
        
        # First thing, check if the coorindates are out of bound or the node has been
        # visited/is an obstacle
        i, j = coord
        if (i < 0) or (j < 0) or (i >= len(grid)) or (j >= len(grid[0])) \\
        or (grid[i][j] < 0):
            return 0
        
        # Otherwise see if we're at the end coordinate
        if grid[i][j] == 2 and count == 0:
            return numPaths + 1
        
        # Otherwise mark this point as visited, or an obstacle
        saved = grid[i][j]
        grid[i][j] = -2
        
        # Do the DFS on the neighbours
        neighbours = [[i + 1, j], [i - 1, j], [i, j + 1], [i, j - 1]]
        for neighbour in neighbours:
            numPaths += self.visitedDFS(grid, neighbour, count - 1)
            
        # Unmark the node
        grid[i][j] = saved
        
        return numPaths
    
    
    
    
        
