class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        (m, n) = (len(mat), len(mat[0]))
        ans = 0
        colCount = [0] * n
        for i in range(m):
            rowCount = 0
            colCount1 = [0] * n
            for j in range(n):
                if mat[i][j]:
                    rowCount += 1
                    colCount1[j] = colCount[j] + 1
                    minColCount = math.inf
                    for k in range(j, j - rowCount, -1):
                        minColCount = min(minColCount, colCount1[k])
                        ans += minColCount
                else:
                    colCount1[j] = 0
                    rowCount = 0
            colCount = colCount1
        return ans
