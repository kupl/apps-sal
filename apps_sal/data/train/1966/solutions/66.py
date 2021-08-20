class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        row = len(mat)
        col = len(mat[0])
        res = 0

        def calculate1dArray(arr):
            ans = 0
            pre = 0
            for (i, a) in enumerate(arr):
                if a == 1:
                    pre += 1
                    ans += pre
                else:
                    pre = 0
            return ans
        for a in range(row):
            arr = [1] * col
            for b in range(a, row):
                for c in range(col):
                    arr[c] &= mat[b][c]
                res += calculate1dArray(arr)
        return res
