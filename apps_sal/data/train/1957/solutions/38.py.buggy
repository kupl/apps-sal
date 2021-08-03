\"\"\"
https://www.youtube.com/watch?v=RQxws-5elag

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
        
        queue = collections.deque([(0, 0, 0, 0)])
        Row, Col = len(grid), len(grid[0])
        visited = set()
         
        while queue:
            r, c, obstacle, steps = queue.popleft()
            for x, y in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= x < Row and 0 <= y < Col:
                    if grid[x][y] == 1 and obstacle < k and (x, y, obstacle + 1) not in visited:
                        visited.add((x, y, obstacle + 1))
                        queue.append((x, y, obstacle + 1, steps + 1))
                    if grid[x][y] == 0 and (x, y, obstacle) not in visited:    
                        if (x, y) == (Row - 1, Col - 1):
                            return steps + 1
                        visited.add((x, y, obstacle))
                        queue.append((x, y, obstacle, steps + 1))
                        
        return -1
