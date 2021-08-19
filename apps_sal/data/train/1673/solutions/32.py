class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        while len(arr) > 1:
            bottom = arr.pop()
            for i in range(len(arr[-1])):
                arr[-1][i] += min((el for (j, el) in enumerate(bottom) if i != j))
        return min(arr[0])
