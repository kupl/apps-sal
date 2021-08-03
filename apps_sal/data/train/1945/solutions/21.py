class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        rows = {}
        max_value = 0
        n = len(matrix)
        for i in range(n):
            if matrix[i][0] == 0:
                a = tuple(matrix[i])
            else:
                a = tuple([1 - c for c in matrix[i]])
           # for j in range(m):
          #      if matrix[i]  # [j]==0:
              #      a+=str(j)
           #     else:
          #          b+=str(j)
            #a = tuple(a)
            #b = tuple(b)
            if a not in rows:
                rows[a] = 0
           # if b not in rows:
         #       rows[b] = 0
            rows[a] += 1

        # rows[b]+=1
            max_value = max(max_value, rows[a])
        return max_value
