class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        parent = {}
        nums = collections.defaultdict(int)
        visited = set()
        res = 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in parent:
                    parent[(i, j)] = (i, j)
                    stack = [(i, j)]
                    while stack:
                        x, y = stack.pop()
                        nums[(i, j)] += 1
                        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                        for direction in directions:
                            dx, dy = direction
                            if self.is_valid(grid, (x + dx, y + dy), parent):
                                parent[(x + dx, y + dy)] = (i, j)
                                stack.append((x + dx, y + dy))

        for v in list(nums.values()):
            res = max(res, v)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    candidates = []
                    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
                    for direction in directions:
                        dx, dy = direction
                        if i + dx < 0 or i + dx >= len(grid) or j + dy < 0 or j + dy >= len(grid[0]):
                            continue
                        # if (i+dx, j+dy) in visited:
                        #     continue
                        if grid[i + dx][j + dy] == 1:
                            continue
                        visited.add((i + dx, j + dy))
                        res = max(res, nums[parent[i, j]] + 1)
                        extra = 1
                        temp_visited = set()
                        for second_direction in directions:
                            ddx, ddy = second_direction
                            if i + dx + ddx < 0 or i + dx + ddx >= len(grid) or j + dy + ddy < 0 or j + dy + ddy >= len(grid[0]):
                                continue
                            if grid[i + dx + ddx][j + dy + ddy] == 0:
                                continue
                            if parent[(i + dx + ddx, j + dy + ddy)] == parent[(i, j)]:
                                continue
                            if parent[(i + dx + ddx, j + dy + ddy)] in temp_visited:
                                continue
                            else:
                                extra += nums[parent[i + dx + ddx, j + dy + ddy]]
                                temp_visited.add(parent[(i + dx + ddx, j + dy + ddy)])

                        res = max(res, nums[parent[i, j]] + extra)

        return res

    def is_valid(self, grid, pos, parent):
        x, y = pos
        if x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0]):
            return False
        if (x, y) in parent:
            return False
        if grid[x][y] == 0:
            return False

        return True
