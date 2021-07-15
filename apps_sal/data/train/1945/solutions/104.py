class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        options = {\"\": 0}
        best = \"\"
        for i in range(len(matrix)):
          option0 = \"\"
          option1 = \"\"
          for j in range(len(matrix[i])):
            if matrix[i][j] == 1:
              option0 = \",\".join([option0, str(j)])
            else:
               option1 = \",\".join([option1, str(j)])
          for option in [option0, option1]:
            if option in options:
              options[option] += 1
            else:
              options[option] = 1
            if options[option] > options[best]:
              best = option
        return options[best]
