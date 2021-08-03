class Solution:
    def minFallingPathSum(self, arr: List[List[int]]) -> int:

        from copy import deepcopy

        v = deepcopy(arr)

        for i in range(len(arr) - 2, -1, -1):
            for j in range(len(arr[0])):
                minn = float('inf')
                for k in range(len(arr[0])):
                    if j != k:
                        minn = min(minn, v[i + 1][k])

                v[i][j] += minn

        return min(v[0])
