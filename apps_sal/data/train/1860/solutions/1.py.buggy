class Solution:
     def fallingSquares(self, positions):
         """
         :type positions: List[List[int]]
         :rtype: List[int]
         """
         to_cor = {}
         for x, l in positions:
             to_cor[x] = 1
             to_cor[x+l] = 1
         for i, v in enumerate(sorted(to_cor.keys())):
             to_cor[v] = i
         over = Overlapper(len(to_cor))
         ans = []
         mx = 0
         for x, l in positions:
             tmx = over.getMax(to_cor[x], to_cor[x+l])+l
             mx = max(mx, tmx)
             ans.append(mx)
             over.Update(to_cor[x], to_cor[x+l], tmx)
         return ans
         
         
 class Overlapper:
     def __init__(self, n):
         self.line = [0]*n
     
     def getMax(self, a, b):
         return max(self.line[a:b])
     
     def Update(self, a, b, mx):
         self.line[a:b] = [mx]*(b-a)
