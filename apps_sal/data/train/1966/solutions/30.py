class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        
        # 生成直方图histogram
        def countOneRow(arr):
            res = 0
            l = 0
            for i in range(len(arr)):
                if arr[i] == 0:
                    l = 0
                else: l = l + 1
                res += l # 以当前为最右，可以形成l个矩形
            return res
        
        rows = len(mat)
        cols = len(mat[0])
        res = 0
        for top in range(rows):
            h = [1] * cols
            l = 0
            for bottom in range(top, rows):
                for c in range(cols):
                    # 每一行都跟top来merge，因为中间必须所有格都是1，才能形成一个矩形
                    h[c] &= mat[bottom][c]
                res += countOneRow(h)
                if not any(h): break
        return res
