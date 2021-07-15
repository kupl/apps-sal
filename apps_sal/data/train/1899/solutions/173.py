class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        def findIslandA(i, j):
          A[i][j] = -1
          islandA.append((i, j))
          for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j+1)):
            if 0 <= x < n and 0 <= y < n and A[x][y] == 1:
              findIslandA(x, y)
              
        def first():
          for i in range(n):
            for j in range(n):
              if A[i][j]:
                return i, j
              
        n, step, islandA = len(A), 0, []
        findIslandA(*first())
        while islandA:
          boundaries = []
          for i, j in islandA:
            for x, y in ((i - 1, j), (i + 1, j), (i, j - 1), (i, j+1)):
              if 0 <= x < n and 0 <= y < n:
                if A[x][y] == 1:
                  return step
                elif A[x][y] == 0:
                  A[x][y] = -1
                  boundaries.append((x, y))
          step += 1
          islandA = boundaries
