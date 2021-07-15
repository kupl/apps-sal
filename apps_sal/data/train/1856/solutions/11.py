class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        stack = [(0, 0, 0, 0, 1)]
        n = len(grid)
        visited = set()
        visited.add((0, 0, 0, 1))

        while stack:
            stepNow, ia, ja, ib, jb = heapq.heappop(stack)
            
            ia1, ja1, ib1, jb1 = ia, ja+1, ib, jb+1
            if jb1 < n and grid[ib1][jb1] == 0 and grid[ia1][ja1] == 0 and (ia1, ja1, ib1, jb1) not in visited:
                if (ia1, ja1, ib1, jb1) == (n-1, n-2, n-1, n-1):
                    return stepNow+1
                visited.add((ia1, ja1, ib1, jb1))
                heapq.heappush(stack, (stepNow + 1, ia1, ja1, ib1, jb1))
            
            ia1, ja1, ib1, jb1 = ia+1, ja, ib+1, jb
            if ia1 < n and ib1 < n and grid[ib1][jb1] == 0 and grid[ia1][ja1] == 0 and (ia1, ja1, ib1, jb1) not in visited:
                if (ia1, ja1, ib1, jb1) == (n-1, n-2, n-1, n-1):
                    return stepNow+1
                visited.add((ia1, ja1, ib1, jb1))
                heapq.heappush(stack, (stepNow + 1, ia1, ja1, ib1, jb1))
            
            if ia == ib and ja == jb-1:
                if ia + 1< n and grid[ia+1][ja] == 0 and grid[ib+1][jb] == 0:
                    ia1, ja1, ib1, jb1 = ia, ja, ia+1, ja
                    if (ia1, ja1, ib1, jb1) not in visited:
                        if (ia1, ja1, ib1, jb1) == (n-1, n-2, n-1, n-1):
                            return stepNow+1
                        visited.add((ia1, ja1, ib1, jb1))
                        heapq.heappush(stack, (stepNow + 1, ia1, ja1, ib1, jb1)) 
            
            if ja == jb and ia == ib-1:
                if ja + 1 < n and grid[ia][ja+1] == 0 and grid[ib][jb+1] == 0:
                    ia1, ja1, ib1, jb1 = ia, ja, ia, ja+1
                    if (ia1, ja1, ib1, jb1) not in visited:
                        if (ia1, ja1, ib1, jb1) == (n-1, n-2, n-1, n-1):
                            return stepNow+1
                        visited.add((ia1, ja1, ib1, jb1))
                        heapq.heappush(stack, (stepNow + 1, ia1, ja1, ib1, jb1)) 
        return -1
