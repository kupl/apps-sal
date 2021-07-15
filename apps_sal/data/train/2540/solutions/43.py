class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
      res = 0
      A.sort()
      for i in range(len(A)):
        for j in range(i+1, len(A)):
          source = A[i]
          target = A[j]
          lower = abs(target - source)
          upper = source + target
          if (upper*2 < res):
            continue
          for t in range(j+1, len(A)):
            if lower < A[t] < upper:
              res = max(source + target + A[t], res)
              break
          if res != 0:
            break
      return res

