class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        T = [[0 for _ in range(len(arr))] for _ in range(len(arr))]
        T[0] = arr[0]
        for i in range(1, len(arr)):
            for j in range(len(arr)):
                T[i][j] = arr[i][j] + min([T[i - 1][c] for c in range(len(arr)) if c != j])
        return min(T[-1])
