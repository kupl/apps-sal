class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        rows = len(mat)
        cols = len(mat[0])
        n = 0
        for top in range(rows):
            for left in range(cols):
                bottom = rows
                for right in range(left, cols):
                    scan = top
                    while scan < bottom and mat[scan][right]:
                        scan += 1
                    bottom = scan
                    n += bottom - top
                    if bottom == top:
                        break
        return n
