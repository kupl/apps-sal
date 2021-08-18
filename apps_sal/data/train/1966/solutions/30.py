class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        def countOneRow(arr):
            res = 0
            l = 0
            for i in range(len(arr)):
                if arr[i] == 0:
                    l = 0
                else:
                    l = l + 1
                res += l
            return res

        rows = len(mat)
        cols = len(mat[0])
        res = 0
        for top in range(rows):
            h = [1] * cols
            l = 0
            for bottom in range(top, rows):
                for c in range(cols):
                    h[c] &= mat[bottom][c]
                res += countOneRow(h)
                if not any(h):
                    break
        return res
