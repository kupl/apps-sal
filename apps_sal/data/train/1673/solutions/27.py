class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        (m, n) = (len(arr), len(arr[0]))
        for i in range(1, m):
            (min1, min2) = (None, None)
            for j in range(n):
                if min1 == None or arr[i - 1][min1] > arr[i - 1][j]:
                    min2 = min1
                    min1 = j
                elif min2 == None or arr[i - 1][min2] > arr[i - 1][j]:
                    min2 = j
            for j in range(n):
                if j == min1:
                    arr[i][j] += arr[i - 1][min2]
                else:
                    arr[i][j] += arr[i - 1][min1]
        return min(arr[-1])
