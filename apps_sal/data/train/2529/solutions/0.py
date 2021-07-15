import itertools

class Solution:
  def numSpecial(self, mat: List[List[int]]) -> int:
    rr = [i for i, r in enumerate(mat) if sum(r) == 1]
    cc = [i for i, c in enumerate(zip(*mat)) if sum(c) == 1]
    return sum(1 for i, j in itertools.product(rr, cc) if mat[i][j] == 1)
