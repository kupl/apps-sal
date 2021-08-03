class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        N = len(arr)
        while len(arr) >= 2:
            cur = arr.pop()
            for i in range(N):
                newa = cur[:i] + cur[i + 1:]
                arr[-1][i] += min(newa)

        return min(arr[0])
