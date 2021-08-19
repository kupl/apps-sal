class Solution:

    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        options = {tuple([]): 0}
        best = tuple([])
        for i in range(len(matrix)):
            option0 = []
            option1 = []
            for j in range(len(matrix[i])):
                if matrix[i][j] == 1:
                    option0.append(j)
                else:
                    option1.append(j)
            for option in [tuple(option0), tuple(option1)]:
                if option in options:
                    options[option] += 1
                else:
                    options[option] = 1
                if options[option] > options[best]:
                    best = option
        return options[best]
