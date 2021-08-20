class Solution:

    def numSubmat(self, mat: List[List[int]]) -> int:
        if not mat:
            return 0
        (m, n) = (len(mat), len(mat[0]))
        prefix = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n - 1, -1, -1):
                if j == n - 1:
                    prefix[i][j] = mat[i][j]
                if mat[i][j] == 0:
                    continue
                if j + 1 <= n - 1:
                    prefix[i][j] = prefix[i][j + 1] + mat[i][j]
        print(prefix)
        count = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                width = prefix[i][j]
                res = width
                for k in range(i + 1, m):
                    if prefix[k][j] <= width:
                        width = prefix[k][j]
                        res += prefix[k][j]
                    else:
                        res += width
                count[i][j] = res
        print(count)
        ans = 0
        for i in range(m):
            ans += sum(count[i])
        return ans
