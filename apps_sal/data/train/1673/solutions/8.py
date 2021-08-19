class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        nRow, nCol = len(arr), len(arr[0])
        # pathSum = [[0] * col for _ in range(row)] # row-by-col 2D array filled with 0
        pathSum = arr.copy()

        for row in range(-2, -nCol - 1, -1):  # bottom-to-top
            for col in range(nCol):  # left-to-right
                pathSum[row][col] += min(pathSum[row + 1][0:col] + pathSum[row + 1][col + 1:])

        return min(pathSum[0])
