class Solution:
    def numSubmat(self, mat: List[List[int]]) -> int:

        # for each row, calculate how many matrices can you build with all ones

        # then for each cell keep increasing height and taking minimum and adding its count

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

        # now we take each cell and increase height one by one and keep adding to the
        # final answer
        ans = 0
        for row in range(len(mat)):
            for col in range(len(mat[0])):
                count = 0
                if mat[row][col]:  # atleast some matrix starts at this point
                    min_width = mat[row][col]
                    for index in range(row, len(mat)):
                        if not mat[index][col]:  # can't expand matrix anymore
                            break
                        min_width = min(min_width, mat[index][col])
                        count += min_width
                ans += count

        return ans
        # keep increasing
