class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:
        m = len(mat)
        if m == 0:
            return 0

        n = len(mat[0])
        if n == 0:
            return 0
        temp = [0, 0]
        count = [[[0] * 2 for l in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    res += mat[i][j]
                    count[i][j][0] = mat[i][j]
                    count[i][j][1] = mat[i][j]
                    continue
                elif i == 0 and mat[i][j]:
                    count[i][j][1] += count[i][j - 1][1] + 1
                    res += count[i][j][1]
                    count[i][j][0] = mat[i][j]
                elif j == 0 and mat[i][j]:
                    count[i][j][0] += count[i - 1][j][0] + 1
                    res += count[i][j][0]
                    count[i][j][1] = mat[i][j]
                elif mat[i][j]:
                    res += 1
                    count[i][j][1] += count[i][j - 1][1] + 1
                    count[i][j][0] += count[i - 1][j][0] + 1
                    if count[i][j - 1][1]:
                        res += count[i][j - 1][1]
                    if count[i - 1][j][0]:
                        res += count[i - 1][j][0]
                    findmin = count[i][j][0]
                    for k in range(1, count[i][j][1]):
                        findmin = min(findmin, count[i][j - k][0])
                    # if count[i][j][0] > 1 and count[i][j][1] > 1 and count[i-1][j-1][0] >= 1:
                    #     # count[i][j][2] =
                    #     # res += min(count[i][j][0], count[i][j][1])-1
                        res += findmin - 1

                # print(i, j, res)
        # print(count)
        return res
