class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        nodes = deque()
        visited = {}
        print((len(grid), len(grid[0])))
        nodes.append([(0, 0), k, 0])
        ans = []
        while nodes:
            x, r, steps = nodes.popleft()
            # print([x, r, steps], end=' ')
            if x[0] == len(grid)-1 and x[1] == len(grid[0])-1:
                ans.append(steps)
                break
            if x in visited and visited[x] >= r:
                continue
            visited[x] = r
            if x[0]>0 and r-grid[x[0]-1][x[1]]>-1:
                nodes.append([(x[0]-1, x[1]), r-grid[x[0]-1][x[1]], steps+1])
            if x[0] < len(grid)-1 and r-grid[x[0]+1][x[1]]>-1:
                nodes.append([(x[0]+1, x[1]), r-grid[x[0]+1][x[1]], steps+1])
            if x[1] > 0 and r-grid[x[0]][x[1]-1]>-1:
                nodes.append([(x[0], x[1]-1), r-grid[x[0]][x[1]-1], steps+1])
            if x[1] < len(grid[0])-1 and r-grid[x[0]][x[1]+1]>-1:
                nodes.append([(x[0], x[1]+1), r-grid[x[0]][x[1]+1], steps+1])
        
        print(ans)
        if not ans:
            return -1
        return min(ans)

