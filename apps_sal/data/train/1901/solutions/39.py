class Solution:
    def largestIsland(self, matrix: List[List[int]]) -> int:
        def move(r, c):
            for ri, ci in [[0,1], [1,0], [0,-1], [-1,0]]:
                rn, cn = r+ri, c+ci
                if 0 <= rn < len(matrix) and 0 <= cn < len(matrix[0]):
                    yield rn, cn
        def dfs(r, c, idx):
            res = 1
            matrix[r][c] = idx
            for rn, cn in move(r, c):
                if matrix[rn][cn] == 1:
                    res += dfs(rn, cn, idx)
            return res
        res = 0
        group = 2
        group_size = {0:0}
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    count = dfs(i, j, group)
                    group_size[group] = count
                    res = max(res, count)
                    group += 1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    # check adj 4
                    adjgrp = set(matrix[r][c] for r,c in move(i,j))
                    res = max(res, sum(group_size[grp] for grp in adjgrp)+1)
        return res            
