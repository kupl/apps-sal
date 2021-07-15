from heapq import *
class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        def is_valid(i, j):
            return 0 <= i < m and 0 <= j < n
            
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        bfs = []
        visited = set()
        heappush(bfs, [0, k, (0, 0)])  # cur_moves, k, position
        while bfs:
            cur_moves, k_left, pos = heappop(bfs)
            i, j = pos
            # if cur_moves >=20:
            #     print(cur_moves, k_left, pos)
            if (i,j,k_left) in visited: continue
            visited.add((i,j,k_left))
            if pos == (m-1, n-1):
                return cur_moves
            
            for di, dj in directions:
                if not is_valid(i+di, j+dj): continue
                if grid[i+di][j+dj] == 1 and k_left > 0:
                    heappush(bfs, [cur_moves+1, k_left-1, (i+di, j+dj)])
                elif grid[i+di][j+dj] == 0:
                    heappush(bfs, [cur_moves+1, k_left, (i+di, j+dj)])
                
        return -1
