import heapq

class Solution:
  def minFallingPathSum(self, arr: List[List[int]]) -> int:
    # O(N^2), N = len(arr) >= 3
    n = len(arr)
    # keep the min and 2nd-min with corresponding index of falling path at each row
    xm = [(0, -1), (0, -1)]
    for i in range(n):
      xm = heapq.nsmallest(2, [(x + xm[1][0], j) if j == xm[0][1] else (x + xm[0][0], j) for j, x in enumerate(arr[i])])
    return xm[0][0]
