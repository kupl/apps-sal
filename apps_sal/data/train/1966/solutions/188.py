class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        if not mat:
            return 0

        for row in range(len(mat)):
            for col in range(len(mat[0])):
                count = 0
                if mat[row][col] == 1:
                    for index in range(col, len(mat[0])):
                        if mat[row][index]:
                            count += 1
                        else:
                            break

                mat[row][col] = count

        ans = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                count = 0
                if mat[row][col]:
                    min_width = mat[row][col]
                    for index in range(row, len(mat)):
                        if not mat[index][col]:
                            break
                        min_width = min(min_width, mat[index][col])
                        count += min_width
                ans += count

        return ans
