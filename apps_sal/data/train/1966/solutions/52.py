class Solution:
    def numSubmat2(self, mat: List[List[int]]) -> int:
        \"\"\"O(m^2*n)\"\"\"
        def calc(arr):
            res = 0
            leng = 0
            for i in range(len(arr)):
                leng = 0 if arr[i] == 0 else leng + 1
                res += leng
            return res
        m, n = len(mat), len(mat[0])
        res = 0
        for i in range(m):
            arr = [1] * n
            for j in range(i, m):
                for k in range(n):
                    arr[k] &= mat[j][k]
                res += calc(arr)
        return res
    
    def numSubmat(self, mat: List[List[int]]) -> int:
        \"\"\"O(m*n^2)\"\"\"
        def calc(arr):
            res = 0
            leng = 0
            for i in range(len(arr)):
                leng = 0 if arr[i] == 0 else leng + 1
                res += leng
            return res
        def calc2(arr):
            res = 0
            for c, g in itertools.groupby(arr):
                if c == 1:
                    n = len(list(g))
                    res += n * (n + 1)//2
            return res
        m, n = len(mat), len(mat[0])
        res = 0
        for i in range(n):
            arr = [1] * m
            for j in range(i, n):
                for k in range(m):
                    arr[k] &= mat[k][j]
                res += calc2(arr)
        return res
