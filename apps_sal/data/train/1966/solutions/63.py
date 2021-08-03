class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])

        def count_sub(i, j):
            max_c = n
            count = 0
            for r in range(i, m):
                for c in range(j, max_c):
                    if mat[r][c] == 1:
                        count += 1
                    else:
                        max_c = c
                        break
            return count

        ans = 0
        for i in range(m):
            for j in range(n):
                if mat[i][j]:
                    ans += count_sub(i, j)
        return ans
