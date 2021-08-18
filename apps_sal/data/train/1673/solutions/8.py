class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        nRow, nCol = len(arr), len(arr[0])
        pathSum = arr.copy()

        for row in range(-2, -nCol - 1, -1):
            for col in range(nCol):
                pathSum[row][col] += min(pathSum[row + 1][0:col] + pathSum[row + 1][col + 1:])

        return min(pathSum[0])
