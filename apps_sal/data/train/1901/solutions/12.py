class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:
        """
        Run DFS to find all islands (marked with unique id) and store their sizes. Then iterate through all zeros to see if a zero connects two islands. 
        DFS also counts the number of nodes in an island.

        Time O(N) - Run DFS to find all connected components takes O(N), and iterate through each zero takes O(1) for each because we only need to check the 4 neighbors of each zero. Total time O(N)
        Space O(N) - worst case, only additional storage is for island_sizes hashmap and zeros hashset, plus some constants.
        """
        island_sizes = {}
        (max_island_id, max_island_size) = (-1, 0)
        global_island_id = 2
        zeros = set()
        deltas = ((1, 0), (-1, 0), (0, 1), (0, -1))
        (rows, cols) = (len(grid), len(grid[0]))

        def dfs(row, col, island_id) -> int:
            if row < 0 or row >= rows or col < 0 or (col >= cols) or (grid[row][col] != 1):
                return 0
            count = 1
            grid[row][col] = island_id
            for (dr, dc) in deltas:
                count += dfs(row + dr, col + dc, island_id)
            return count
        for (r, row) in enumerate(grid):
            for (c, val) in enumerate(row):
                if val == 1:
                    cur_size = dfs(r, c, global_island_id)
                    island_sizes[global_island_id] = cur_size
                    if cur_size > max_island_size:
                        max_island_size = cur_size
                        max_island_id = global_island_id
                    global_island_id += 1
                elif val == 0:
                    zeros.add((r, c))
        if not zeros:
            return max_island_size
        for (r, c) in zeros:
            cur_max_size = 1
            islands_seen = set()
            for (dr, dc) in deltas:
                (nr, nc) = (r + dr, c + dc)
                if 0 <= nr < rows and 0 <= nc < cols:
                    cur_val = grid[nr][nc]
                    if cur_val in island_sizes and cur_val not in islands_seen:
                        islands_seen.add(cur_val)
                        cur_max_size += island_sizes[cur_val]
            max_island_size = max(max_island_size, cur_max_size)
        return max_island_size
