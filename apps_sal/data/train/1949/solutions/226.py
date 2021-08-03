class Solution:
    def getMaximumGold(self, g: List[List[int]]) -> int:
        def dfs(i, j, visited):
            if not (0 <= i < len(g) and 0 <= j < len(g[0]) and g[i][j] != 0 and (i, j) not in visited):
                return 0
            visited.add((i, j))
            res = g[i][j] + max(0, max(dfs(i + x, j + y, visited) for x, y in [[-1, 0], [1, 0], [0, 1], [0, -1]]))
            visited.remove((i, j))
            return res
        return max(dfs(i, j, set()) for i in range(len(g)) for j in range(len(g[0])))
