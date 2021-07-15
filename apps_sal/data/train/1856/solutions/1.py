class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n = len(grid)
        q = collections.deque([(0, 0, 0, 1, 0)])
        visited = set([(0, 0, 0, 1)])
        while q: 
            tailx, taily, headx, heady, steps = q.popleft()
            if (tailx == n-1 and taily == n-2 and headx == n-1 and heady == n-1):
                return steps
            for n_tailx, n_taily, n_headx, n_heady in (
                (tailx, taily+1, headx, heady+1),
                (tailx+1, taily, headx+1, heady)): 
                if (0 <= n_tailx < n and 0<= n_taily < n  and
                    0 <= n_headx < n and 0<= n_heady <n  and
                    (n_tailx, n_taily, n_headx, n_heady) not in visited and
                    grid[n_headx][n_heady] == 0 and grid[n_tailx][n_taily] == 0):
                    visited.add((n_tailx, n_taily, n_headx, n_heady))
                    #print(\"lr\", (n_tailx, n_taily, n_headx, n_heady, steps + 1)) 
                    q.append((n_tailx, n_taily, n_headx, n_heady, steps + 1))
            if (tailx == headx):
                if (tailx + 1 < n and 
                    grid[tailx + 1][taily] == 0 and 
                    grid[headx + 1][heady] == 0 and 
                    (tailx, taily, tailx+1, taily) not in visited):
                    visited.add((tailx, taily, tailx+1, taily))
                    #print(\"rc\",(tailx, taily, tailx+1, taily, steps + 1))
                    q.append((tailx, taily, tailx+1, taily, steps + 1))
            if (taily == heady):
                if (taily + 1 < n and 
                    grid[tailx][taily + 1] == 0 and 
                    grid[headx][heady +1] == 0 and 
                    (tailx, taily, tailx, taily+1) not in visited):
                    visited.add((tailx, taily, tailx, taily+1))
                    #print(\"rcc\",(tailx, taily, tailx, taily+1, steps + 1))
                    q.append((tailx, taily, tailx, taily+1, steps + 1))
                    
        return -1
                    
                    
            

