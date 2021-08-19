class Solution:

    def minFallingPathSum(self, arr: List[List[int]]) -> int:
        n = len(arr)

        def getTwo(a):
            pos = {v: k for (k, v) in enumerate(a)}
            (f, s) = sorted(a)[:2]
            return ([f, pos[f]], [s, pos[s]])
        for i in range(1, n):
            pre = getTwo(arr[i - 1])
            for j in range(n):
                if j != pre[0][1]:
                    arr[i][j] += pre[0][0]
                else:
                    arr[i][j] += pre[1][0]
        return min(arr[-1])
