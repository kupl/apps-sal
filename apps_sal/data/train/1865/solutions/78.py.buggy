class Solution:
    FLOOR = \".\"
    WALL = \"#\"
    def minPushBox(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        player, box, target = (0, 0), (0, 0), (0, 0)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == \"S\": player = (i, j)
                if grid[i][j] == \"B\": box = (i, j)
                if grid[i][j] == \"T\": target = (i, j)
        print(box, target)
        
        hq = [(abs(target[0] - box[0]) + abs(target[1] - box[1]), 0, box, player)]
        steps = collections.defaultdict(int)
        # steps[box] = 0
        
        while len(hq) > 0:
            curr_heuristic_est, curr_steps, (curr_i, curr_j), player = heappop(hq)
            print(curr_heuristic_est, curr_steps, (curr_i, curr_j), player)
            if (curr_i, curr_j) == target:
                return curr_steps
            
            for next_i, next_j in self._get_next(grid, curr_i, curr_j, player):
                if (((next_i, next_j), (curr_i, curr_j))) not in steps or curr_steps + 1 < steps[((next_i, next_j), (curr_i, curr_j))]:
                    player = (curr_i, curr_j)
                    steps[((next_i, next_j), (curr_i, curr_j))] = curr_steps + 1
                    heappush(hq, (curr_steps + 1 + abs(target[0]-next_i) + abs(target[1]-next_j), curr_steps + 1, (next_i, next_j), player))
                    
        return -1
                   
        
    def _get_next(self, grid, curr_i, curr_j, player):
        \"\"\"
        Return a list of posible positions the box could be moved to. There are basically 4 choices
        \"\"\"
        m, n = len(grid), len(grid[0])
        res = []
        if (curr_i, curr_j) == (2, 1):
            print(curr_i, curr_j, grid[curr_i - 1][curr_j], player)
        if curr_i - 1 >= 0 and grid[curr_i - 1][curr_j] != self.WALL and self._can_player_reach(grid, player, (curr_i + 1, curr_j), (curr_i, curr_j), set()):
            res.append((curr_i - 1, curr_j))
        if (curr_i, curr_j) == (2, 1):
            print(res)
        if curr_i + 1 < m and grid[curr_i + 1][curr_j] != self.WALL and self._can_player_reach(grid, player, (curr_i - 1, curr_j), (curr_i, curr_j), set()):
            res.append((curr_i + 1, curr_j))
        if curr_j - 1 >= 0 and grid[curr_i][curr_j - 1] != self.WALL and self._can_player_reach(grid, player, (curr_i, curr_j + 1), (curr_i, curr_j), set()):
            res.append((curr_i, curr_j - 1))
        if curr_j + 1 < n and grid[curr_i][curr_j + 1] != self.WALL and self._can_player_reach(grid, player, (curr_i, curr_j - 1), (curr_i, curr_j), set()):
            res.append((curr_i, curr_j + 1))
        return res
    
    
    def _can_player_reach(self, grid, curr_pos, dst, box, visited):
        \"\"\"
        Return if player can reach dst position by doing bfs/dfs
        \"\"\"
        m, n = len(grid), len(grid[0])
        if curr_pos[0] < 0 or curr_pos[0] >= m or curr_pos[1] < 0 or curr_pos[1] >= n:
            return False
        if dst == (3, 1):
            print(curr_pos, \"ha\")
        if curr_pos == dst:
            return True
        
        for delta_i, delta_j in [(1, 0), (0, -1), (-1, 0), (0, 1)]:
            next_i, next_j = curr_pos[0] + delta_i, curr_pos[1] + delta_j
            if 0 <= next_i < m and 0 <= next_j < n:
                if grid[next_i][next_j] != self.WALL:
                    if (next_i, next_j) not in visited and (next_i, next_j) != box:
                        visited.add((next_i, next_j))
                        if self._can_player_reach(grid, (next_i, next_j), dst, box, visited):
                            return True
        return False
