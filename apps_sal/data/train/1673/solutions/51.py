class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)
        dp1 = [None for i in range(n)]
        for i in range(0, n):
            dp1[i] = arr[0][i]
        for i in range(1, n):
            dp2 = [None for i in range(n)]
            for j in range(0, n):
                minList = []
                for k in range(0, n):
                    if k == j:
                        continue
                    minList.append(dp1[k])
                dp2[j] = min(minList) + arr[i][j]
            dp1 = dp2
        return min(dp2)
