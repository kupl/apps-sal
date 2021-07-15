\"\"\"
try permutation removal of k obstacles and find the shortest way in each removal

time complexy = (n ^ k) * size(board)

dp[row][col][k] = to get (row, col) with removing k obstacles, shortest cost

0110000
0110110
0000110

2 steps , removing 2 obstacles
9 steps , removing 0 obstacle

bfs (0, 0, 0, 0) # row, col, number removed obstacle, step
(1, 0, 0, 1)
bfs -> row, col
def bfs(grid, max_k):
    row = len(grid)
    if not row:
        return -1
    col = len(grid[0])
    if not col:
        return -1
        
    cost = [[[-1 for _ in range(k + 1)] for _ in range(col)] for _ in range(row)]
    
    q = deque()
    q.append((0, 0, 0, 0))
    while q:
        r, c, step, k = q.popleft()
        if cost[r][c][k] != -1:
            continue
        cost[r][c][k] = step
        for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nr, nc = dr + r, dc + c
            # check boundary
            if grid[nr][nc] == 1:
                if k == max_k:
                    conitnue
                if cost[nr][nc][k + 1] == -1:
                    cost[nr][nc][k + 1] = step + 1
                    q.append((nr, nc, k + 1, step + 1))
            else:
                if cost[nr][nc][k] == -1:
                    cost[nr][nc][k] = step + 1
                    q.append((nr, nc, k, step + 1))
                
    return min(cost[row - 1][col - 1])
    
\"\"\"

class Solution:
    def shortestPath(self, grid: List[List[int]], max_k: int) -> int:
        row = len(grid)
        if not row:
            return -1
        col = len(grid[0])
        if not col:
            return -1
        
        MAX_STEP = row * col + 1
        
        visited_min_removal = [[MAX_STEP for _ in range(col)] for _ in range(row)]
        cost = [[[MAX_STEP for _ in range(max_k + 1)] for _ in range(col)] for _ in range(row)]
        visited_min_removal[0][0] = 0
        cost[0][0][0] = 0

        q = deque()
        q.append((0, 0, 0, 0)) # row, col, number removed obstacle, step
        while q:
            r, c, k, step  = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = dr + r, dc + c
                if not (0 <= nr < row and 0 <= nc < col):
                    continue
                if grid[nr][nc] == 1:
                    if k == max_k:
                        continue
                    if visited_min_removal[nr][nc] > k + 1:
                        cost[nr][nc][k + 1] = step + 1
                        visited_min_removal[nr][nc] = k + 1
                        q.append((nr, nc, k + 1, step + 1))
                else:
                    if cost[nr][nc][k] == MAX_STEP:
                        cost[nr][nc][k] = step + 1
                        visited_min_removal[nr][nc] = k
                        q.append((nr, nc, k, step + 1))

        ans = min(cost[row - 1][col - 1])
        if ans == MAX_STEP:
            return -1
        else:
            return ans
