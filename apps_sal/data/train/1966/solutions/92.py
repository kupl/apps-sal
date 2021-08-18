class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        m, n = len(mat), len(mat[0])
        left_ones = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    left_ones[i][j] = 0
                else:
                    left_ones[i][j] = 1
                    if j > 0:
                        left_ones[i][j] += left_ones[i][j - 1]

        ans = 0
        for j in range(n):
            Q = list()
            total = 0
            for i in range(m):
                height = 1
                while Q and Q[-1][0] > left_ones[i][j]:
                    total -= Q[-1][1] * (Q[-1][0] - left_ones[i][j])
                    height += Q[-1][1]
                    Q.pop()
                total += left_ones[i][j]
                ans += total
                Q.append((left_ones[i][j], height))

        return ans
