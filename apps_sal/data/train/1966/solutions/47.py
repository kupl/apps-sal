class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        info = [[[] for i in range(len(mat[0]))]for j in range(len(mat))]

        result = 0
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if i == 0 and j == 0:
                    info[i][j].append(mat[i][j])
                    result += mat[i][j]
                elif i == 0 and j != 0:
                    if mat[i][j] == 1:
                        info[i][j].append(info[i][j - 1][0] + 1)
                        result += info[i][j][0]
                    else:
                        info[i][j].append(0)
                elif j == 0 and i != 0:
                    if mat[i][j] == 1:
                        info[i][j].append(1)
                        if mat[i - 1][j] == 1:
                            info[i][j] += info[i - 1][j]
                        result += sum(info[i][j])
                    else:
                        info[i][j].append(0)
                else:
                    if mat[i][j] == 1:
                        info[i][j].append(info[i][j - 1][0] + 1)
                        if mat[i - 1][j] == 1:
                            for index in range(len(info[i - 1][j])):
                                if index + 1 < len(info[i][j - 1]):
                                    info[i][j].append(min(info[i][j - 1][index + 1] + 1, info[i - 1][j][index]))
                                else:
                                    info[i][j].append(1)
                        result += sum(info[i][j])
                    else:
                        info[i][j].append(0)

        return result
