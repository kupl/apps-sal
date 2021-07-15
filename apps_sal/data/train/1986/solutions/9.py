class Solution:
    def helper(self, n):
      if n == 1:
        return ['0', '1']
      else:
        res = self.helper(n-1)
        return ['0' + x for x in res] + ['1' + x for x in res[::-1]]
      
    def circularPermutation(self, n: int, start: int) -> List[int]:
      res = [(int)(n,2) for n in self.helper(n)]
      return res[res.index(start):] + res[:res.index(start)]
