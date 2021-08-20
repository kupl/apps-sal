class Solution:

    def diagonalSum(self, mat: List[List[int]]) -> int:
        leng = len(mat[0])
        ans = 0
        check = [[0 for _ in range(len(mat[0]))] for _ in range(len(mat))]
        for i in range(leng):
            ans += mat[i][i]
            check[i][i] = 1
        for i in range(leng):
            if check[i][leng - 1] != 1:
                ans += mat[i][leng - 1]
            leng -= 1
        return ans
