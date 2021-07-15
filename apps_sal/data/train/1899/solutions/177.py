class Solution:
    def shortestBridge(self, A):
        
        
        # This function is used to find the first index equal to one
        # Will be the first island's root node
        def first():
            for i in range(n):
                for j in range(n):
                    if A[i][j]:
                        return i, j
        
        # Depth first search (recursive)
        def dfs(i, j):
            # Mark all seen elements with -1 so we don't look at them again
            A[i][j] = -1
            # Append element to bfs list
            bfs.append((i, j))
            # Look at all points around (i,j)
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                # If point is feasable and its part of the island, apply dfs again
                if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
                    dfs(x, y)

        n, step, bfs = len(A), 0, []
        # Populate bfs list (first island)
        dfs(*first())
        # Idea is to look at all points contiguous to the first island, and store them in
        # new list, while marking them as seen (-1)
        # Now you cycle through this new list, and see if you touch the second island (any
        # point = 1) If not, need another step and repeat
        while bfs:
            new = []
            # Cycle through all the points
            for i, j in bfs:
                for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)):
                    if 0 <= x < n and 0 <= y < n:
                        if A[x][y] == 1:
                            return step
                        elif not A[x][y]:
                            A[x][y] = -1
                            new.append((x, y))
            step += 1
            bfs = new
        

