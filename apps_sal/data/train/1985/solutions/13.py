class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        def helper(matrix, target, i_base=0, j_base=0):

            if len(matrix) == 0:
                return False

            if len(matrix) < 4 and len(matrix[0]) < 4:
                for i in range(0, len(matrix)):
                    for j in range(0, len(matrix[0])):
                        if matrix[i][j] == target:
                            print(("(" + str(i_base + i) + "," + str(j_base + j) + ")"))
                            return True
                return False

            else:
                cmp = matrix[len(matrix) // 2][len(matrix[0]) // 2]

                if cmp == target:
                    print(("(" + str(i_base + len(matrix) // 2) + "," + str(j_base + len(matrix[0]) // 2) + ")"))
                    return True

                quadrant2 = []
                quadrant3 = []

                for i in range(0, len(matrix) // 2):
                    quadrant2.append(matrix[i][len(matrix[0]) // 2 + 1:])

                for i in range(len(matrix) // 2 + 1, len(matrix)):
                    quadrant3.append(matrix[i][0:len(matrix[0]) // 2])

                if target <= cmp:
                    quadrant1 = []

                    for i in range(0, len(matrix) // 2 + 1):
                        quadrant1.append(matrix[i][0:len(matrix[0]) // 2 + 1])

                    return helper(quadrant1, target, i_base, j_base) or helper(quadrant2, target, i_base, j_base + len(matrix[0]) // 2 + 1) or helper(quadrant3, target, i_base + len(matrix) // 2 + 1, j_base)

                else:
                    quadrant4 = []

                    for i in range(len(matrix) // 2, len(matrix)):
                        quadrant4.append(matrix[i][len(matrix[0]) // 2:])

                    return helper(quadrant4, target, i_base + len(matrix) // 2, j_base + len(matrix[0]) // 2) or helper(quadrant2, target, i_base, j_base + len(matrix[0]) // 2 + 1) or helper(quadrant3, target, i_base + len(matrix) // 2 + 1, j_base)

        out = helper(matrix, target)
        if out == False:
            print("(-1, -1)")

        return out
