class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        innerQueue = deque()
        innerQueue.append((0,0,0,0))
        
        gridSet = set()  # i, j, obstacle
        gridSet.add((0,0,0))
        directions = [[-1,0], [0, -1], [1,0], [0, 1]]
        ans = -1
            
        while len(innerQueue) > 0:
            i, j, obstacle, distance = innerQueue.popleft()
            if i == len(grid) -1 and j == len(grid[0]) - 1:
                ans = distance
                return ans
            
            for direction in directions:
                ni = i + direction[0]
                nj = j + direction[1]
                
                if ni >= 0 and nj >= 0 and ni <len(grid) and nj < len(grid[0]):
                    if grid[ni][nj] == 1 and (ni, nj, obstacle + 1) not in gridSet and obstacle + 1 <= k:
                        gridSet.add((ni, nj, obstacle + 1))
                        innerQueue.append((ni, nj, obstacle + 1, distance + 1))
                    elif grid[ni][nj]== 0 and (ni, nj, obstacle) not in gridSet:
                        gridSet.add((ni, nj, obstacle))
                        innerQueue.append((ni, nj, obstacle, distance + 1))
            
            
        
        return ans
