class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        inf = 2000000000
        m, n = len(arr), len(arr[0])
        res = [[inf] * n for _ in range(m)]
        res[0] = arr[0]
        for i in range(1, m):
            for j in range(n):
                last = min(res[i - 1][:j]) if j > 0 else inf
                last = min(last, min(res[i - 1][j + 1:])) if j < n - 1 else last
                res[i][j] = last + arr[i][j]
        print(res)
        return min(res[-1])
