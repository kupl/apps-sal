import copy


class Solution:
    def helper(self, grid, start_i, start_j, current_gold, visited):
        candidates = []
        current_gold += grid[start_i][start_j]
        visited[(start_i, start_j)] = 1
        if max(0, start_i - 1) != start_i and grid[start_i - 1][start_j] > 0 and (start_i - 1, start_j) not in visited:
            candidates.append((start_i - 1, start_j))
        if min(len(grid) - 1, start_i + 1) != start_i and grid[start_i + 1][start_j] > 0 and (start_i + 1, start_j) not in visited:
            candidates.append((start_i + 1, start_j))
        if max(0, start_j - 1) != start_j and grid[start_i][start_j - 1] > 0 and (start_i, start_j - 1) not in visited:
            candidates.append((start_i, start_j - 1))
        if min(len(grid[0]) - 1, start_j + 1) != start_j and grid[start_i][start_j + 1] > 0 and (start_i, start_j + 1) not in visited:
            candidates.append((start_i, start_j + 1))
        res = 0
        if not candidates:
            return current_gold
        for can in candidates:
            res = max(res, self.helper(grid, can[0], can[1], current_gold, dict(visited)))
        return res

    def getMaximumGold(self, grid: List[List[int]]) -> int:
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                start_i = i
                start_j = j
                counter = 0
                if max(0, start_i - 1) != start_i and grid[start_i - 1][start_j] > 0:
                    counter += 1
                if min(len(grid) - 1, start_i + 1) != start_i and grid[start_i + 1][start_j] > 0:
                    counter += 1
                if max(0, start_j - 1) != start_j and grid[start_i][start_j - 1] > 0:
                    counter += 1
                if min(len(grid[0]) - 1, start_j + 1) != start_j and grid[start_i][start_j + 1] > 0:
                    counter += 1
                if counter <= 2:
                    dicts = {}
                    res = max(res, self.helper(grid, i, j, 0, dicts))
                #print (dicts)
        return res
