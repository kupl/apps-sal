class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        arr = mat.copy()
        for i in range(n):
            c = 0
            for j in range(m):
                if mat[i][j]:
                    c += 1
                else:
                    c = 0
                arr[i][j] = c

        ans = 0
        for i in range(n):
            for j in range(m):
                x = sys.maxsize
                for k in range(i, n):
                    x = min(x, arr[k][j])
                    ans += x

        return ans
