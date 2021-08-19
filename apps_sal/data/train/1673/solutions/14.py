class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        for i in range(1, n):
            for j in range(n):
                prevmin = min(arr[i - 1])
                temp = arr[i - 1][:]
                temp.remove(prevmin)
                prevmin2 = min(temp)
                arr[i][j] += prevmin if prevmin != arr[i - 1][j] else prevmin2
        return min(arr[n - 1])
