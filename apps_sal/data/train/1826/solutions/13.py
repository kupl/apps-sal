

class Solution:
    def matrixBlockSum(self, mat: List[List[int]], K: int) -> List[List[int]]:
        blockSum = [[0] * len(mat[0]) for _ in range(len(mat))]

        accumSum = [[0] * (len(mat[0]) + 1) for _ in range(len(mat) + 1)]
        for x in range(len(mat)):
            for y in range(len(mat[0])):
                accumSum[x + 1][y + 1] = (accumSum[x][y + 1] if x >= 0 else 0) + (accumSum[x + 1][y] if y >= 0 else 0) - (accumSum[x][y] if x >= 0 and y >= 0 else 0) + mat[x][y]

        for x in range(len(mat)):
            for y in range(len(mat[0])):
                blockSum[x][y] = accumSum[max(x - K, 0)][max(y - K, 0)] + accumSum[min(x + K + 1, len(mat))][min(y + K + 1, len(mat[0]))] - accumSum[max(x - K, 0)][min(y + K + 1, len(mat[0]))] - accumSum[min(x + K + 1, len(mat))][max(y - K, 0)]

        return blockSum
