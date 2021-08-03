class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        while(len(arr) >= 2):
            row = arr.pop()
            for i in range(len(row)):
                r = row[:i] + row[i + 1:]
                arr[-1][i] += min(r)
        return min(arr[0])
