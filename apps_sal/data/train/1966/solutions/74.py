class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat or not mat[0]:
            return 0
        (m, n) = (len(mat), len(mat[0]))
        hts = [0] * n
        ans = 0
        for i in range(m):
            for j in range(n):
                hts[j] = hts[j] + 1 if mat[i][j] else 0
            for j in range(n):
                minh = m
                for k in range(j, n):
                    minh = min(minh, hts[k])
                    ans += minh
        return ans
