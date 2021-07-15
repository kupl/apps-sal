\"\"\"
Because we are trying to find the shortest path, use BFS here to exit immediately when a path reaches the bottom right most cell.
Use a set to keep track of already visited paths. We only need to keep track of the row, column, and the eliminate obstacle usage count. We don't need to keep track of the steps because remember we are using BFS for the shortest path. That means there is no value storing a 4th piece of the data, the current steps. This will reduce the amount of repeat work.
m = rows
n = columns
k = allowed elimination usages

Time Complexity
O(m*n*k) time complexity
This is because for every cell (m*n), in the worst case we have to put that cell into the queue/bfs k times.

Runtime: 68 ms, faster than 33.33% of Python3 online submissions

Space Complexity
O(m*n*k) space complexity
This is because for every cell (m*n), in the worst case we have to put that cell into the queue/bfs k times which means we need to worst case store all of those steps/paths in the visited set.
\"\"\"
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        if len(grid) == 1 and len(grid[0]) == 1:
            return 0
        
        q = collections.deque([(0, 0, 0, 0)])
        m, n = len(grid), len(grid[0])
        visited = set()
         
        while q:
            x, y, obstacle, path = q.popleft()
            for i, j in ((x+1, y), (x-1, y), (x, y+1), (x, y-1)):
                if 0 <= i < m and 0 <= j < n:
                    if grid[i][j] == 1 and obstacle < k and (i, j, obstacle + 1) not in visited:
                        visited.add((i, j, obstacle + 1))
                        q.append((i, j, obstacle + 1, path + 1))
                    if grid[i][j] == 0 and (i, j, obstacle) not in visited:    
                        if (i, j) == (m - 1, n - 1):
                            return path + 1
                        visited.add((i, j, obstacle))
                        q.append((i, j, obstacle, path + 1))
                        
        return -1
