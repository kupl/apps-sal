class Solution:

    def largestIsland(self, grid: List[List[int]]) -> int:

        def markIsland(grid, pos, root, d):
            i = pos[0]
            j = pos[1]
            if pos in d.get(root, set()):
                return
            if root not in d:
                d[root] = set()
            d[root].add(pos)
            if i > 0 and grid[i - 1][j] == 1:
                markIsland(grid, (i - 1, j), root, d)
            if i < len(grid) - 1 and grid[i + 1][j] == 1:
                markIsland(grid, (i + 1, j), root, d)
            if j > 0 and grid[i][j - 1] == 1:
                markIsland(grid, (i, j - 1), root, d)
            if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                markIsland(grid, (i, j + 1), root, d)
            if pos == root:
                for entry in d[root]:
                    grid[entry[0]][entry[1]] = len(d[root])
            return

        def checkBranch(grid, pos, pos_dict, checked):

            def getSurrounding(grid, pos, pos_dict, checked):
                if pos in checked:
                    return checked[pos]
                visited = set()
                i = pos[0]
                j = pos[1]
                ret = 1
                if i > 0 and grid[i - 1][j] != 0 and (pos_dict[i - 1, j] not in visited):
                    visited.add(pos_dict[i - 1, j])
                    ret += grid[i - 1][j]
                if i < len(grid) - 1 and grid[i + 1][j] != 0 and (pos_dict[i + 1, j] not in visited):
                    visited.add(pos_dict[i + 1, j])
                    ret += grid[i + 1][j]
                if j > 0 and grid[i][j - 1] != 0 and (pos_dict[i, j - 1] not in visited):
                    visited.add(pos_dict[i, j - 1])
                    ret += grid[i][j - 1]
                if j < len(grid[i]) - 1 and grid[i][j + 1] != 0 and (pos_dict[i, j + 1] not in visited):
                    visited.add(pos_dict[i, j + 1])
                    ret += grid[i][j + 1]
                checked[pos] = ret
                return ret
            i = pos[0]
            j = pos[1]
            max_connect = 1
            if i > 0 and grid[i - 1][j] == 0:
                max_connect = max(max_connect, getSurrounding(grid, (i - 1, j), pos_dict, checked))
            if i < len(grid) - 1 and grid[i + 1][j] == 0:
                max_connect = max(max_connect, getSurrounding(grid, (i + 1, j), pos_dict, checked))
            if j > 0 and grid[i][j - 1] == 0:
                max_connect = max(max_connect, getSurrounding(grid, (i, j - 1), pos_dict, checked))
            if j < len(grid[i]) - 1 and grid[i][j + 1] == 0:
                max_connect = max(max_connect, getSurrounding(grid, (i, j + 1), pos_dict, checked))
            return max_connect
        d = dict()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    markIsland(grid, (i, j), (i, j), d)
        max_size = 1
        pos_dict = dict()
        for (key, value) in d.items():
            max_size = max(max_size, len(value))
            for pos in value:
                pos_dict[pos] = key
        checked = dict()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                max_size = max(max_size, checkBranch(grid, (i, j), pos_dict, checked))
        return max_size
